import json
import subprocess
import sys
import OSFind
import TypeFind

class DetailScan:
    def __init__(self, input_file='PingScanResult.json', output_file='OSScanResult.json'):
        self.input_file = input_file
        self.output_file = output_file

    def read_ip_addresses(self):
        try:
            with open(self.input_file, 'r') as file:
                data = json.load(file)
            return [host['host'] for host in data.get('hosts', [])]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading IP addresses from {self.input_file}: {e}")
            return []

    def run_device_scan(self, ip_addresses):
        scan_results = {'hosts': []}

        for ip in ip_addresses:
            print(f"OS Scanning for {ip}")
            command = ["nmap", "-O", "-Pn", "-T5", ip]

            try:
                result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                if result.returncode != 0:
                    print(f"Error executing nmap for {ip}:\n{result.stderr.strip()}")
                    continue

                print(result.stdout)
                scan_results['hosts'].append(self.parse_nmap_output(ip, result.stdout))

            except Exception as e:
                print(f"Exception occurred while scanning {ip}: {e}")

        return scan_results

    def parse_nmap_output(self, ip, output):
        os_info = OSFind.identify_OS(output)
        device_type = TypeFind.identify_type(output)
        return {
            "host": ip,
            "OS": os_info,
            "Device Type": device_type
        }

    def save_results(self, scan_results):
        try:
            with open(self.output_file, 'w') as file:
                json.dump(scan_results, file, indent=4)
            print(f"Device scan results saved to {self.output_file}")
        except IOError as e:
            print(f"Error saving scan results to {self.output_file}: {e}")

    def detailedScan(self):
        ip_addresses = self.read_ip_addresses()
        if not ip_addresses:
            print("No IP addresses found to scan.")
            sys.exit(1)

        scan_results = self.run_device_scan(ip_addresses)
        self.save_results(scan_results)

if __name__ == "__main__":
    scanner = DetailScan()
    scanner.detailedScan()
