import json
import subprocess
import sys
import OSFind
import TypeFind

def read_ip_addresses(filename='PingScanResult.json'):
    with open(filename, 'r') as file:
        data = json.load(file)
    return [host['host'] for host in data['hosts']]

def run_device_scan(ip_addresses):
    scan_results = {'hosts': []}
    for ip in ip_addresses:
        print(f"OS Scanning for {ip}")
        command = ["nmap", "-O", "-Pn", "-T5", ip]
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.stderr:
                print(f"Error executing nmap for {ip}:", result.stderr)
            else:
                scan_results['hosts'].append(parse_nmap_output(ip, result.stdout))
                print(result.stdout)
        except Exception as e:
            print(f"An error occurred while executing nmap for {ip}:", str(e))
    return scan_results

def parse_nmap_output(ip, output):#Scan the JSON file
    os_info = OSFind.identify_OS(output)
    device_type = TypeFind.identify_type(output)
    return {"host": ip, "OS": os_info, "Device Type": device_type}

def save_results(scan_results, filename='OSScanResult.json'):
    with open(filename, 'w') as file:
        json.dump(scan_results, file, indent=4)
    print(f"Device scan results saved to {filename}")

def detailedScan():
    ip_addresses = read_ip_addresses()
    if not ip_addresses:
        print("No IP addresses found to scan.")
        sys.exit(1)
    scan_results = run_device_scan(ip_addresses)
    save_results(scan_results)
