import json
import subprocess
from .os_find import identify_OS
from .type_find import identify_type

def read_ip_addresses(filename='PingScanResult.json'):
    with open(filename, 'r') as file:
        data = json.load(file)
    return [host['host'] for host in data.get('hosts', [])]

def run_os_scan(ip):
    command = ["nmap", "-O", "-Pn", "-T5", ip]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    return result.stdout

def run_detailed_scan():
    ip_addresses = read_ip_addresses()
    scan_results = {"hosts": []}
    for ip in ip_addresses:
        output = run_os_scan(ip)
        os_info = identify_OS(output)
        device_type = identify_type(output)
        scan_results['hosts'].append({
            "host": ip,
            "OS": os_info,
            "Device Type": device_type
        })
    with open('OSScanResult.json', 'w') as f:
        json.dump(scan_results, f, indent=4)
    return scan_results

