import subprocess
import json

def run_ping_scan(target):
    command = ["nmap", "-sP", target]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    return result.stdout

def parse_nmap_output(output):
    scan_results = {"hosts": []}
    lines = output.split("\n")
    host_info = {}
    for line in lines:
        if "Nmap scan report for" in line:
            if host_info:
                scan_results["hosts"].append(host_info)
                host_info = {}
            host = line.split(" ")[-1]
            if "(" in host and ")" in host:
                host = host[host.find("(")+1:host.find(")")]
            host_info = {"host": host, "status": "up", "manufacturer": "Unknown"}
        elif "MAC Address:" in line:
            parts = line.split(" ", 3)
            if len(parts) > 2:
                host_info["mac"] = parts[2]
                host_info["manufacturer"] = parts[3].strip("()") if len(parts) == 4 else "Unknown"
    if host_info:
        scan_results["hosts"].append(host_info)
    return scan_results

def save_ping_results(scan_results, filename='PingScanResult.json'):
    with open(filename, 'w') as f:
        json.dump(scan_results, f, indent=4)