import json
import subprocess
import sys
import OSFind
import TypeFind

def read_ip_addresses(filename='PingScanResult.json'):
    """
    Reads IP addresses from a JSON file.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return [host['host'] for host in data.get('hosts', [])]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"[ERROR] Failed to read {filename}: {e}")
        return []

def run_device_scan(ip_addresses):
    """
    Runs OS detection on each IP address using nmap.
    """
    scan_results = {'hosts': []}
    for ip in ip_addresses:
        print(f"[INFO] Scanning {ip} for OS...")
        command = ["nmap", "-O", "-Pn", "-T5", ip]
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                print(f"[ERROR] nmap scan failed for {ip}:\n{result.stderr.strip()}")
                continue
            print(f"[INFO] nmap output for {ip}:\n{result.stdout}")
            scan_results['hosts'].append(parse_nmap_output(ip, result.stdout))
        except Exception as e:
            print(f"[EXCEPTION] Error scanning {ip}: {e}")
    return scan_results

def parse_nmap_output(ip, output):
    """
    Extracts OS and device type information from nmap output.
    """
    os_info = OSFind.identify_OS(output)
    device_type = TypeFind.identify_type(output)
    return {
        "host": ip,
        "OS": os_info,
        "Device Type": device_type
    }

def save_results(scan_results, filename='OSScanResult.json'):
    """
    Saves the scan results to a JSON file.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(scan_results, file, indent=4)
        print(f"[SUCCESS] Results saved to {filename}")
    except IOError as e:
        print(f"[ERROR] Failed to save results: {e}")

def detailedScan():
    """
    Runs the full scan process: read IPs → scan → save results.
    """
    ip_addresses = read_ip_addresses()
    if not ip_addresses:
        print("[ERROR] No IP addresses found to scan.")
        sys.exit(1)
    scan_results = run_device_scan(ip_addresses)
    save_results(scan_results)

if __name__ == "__main__":
    detailedScan()
