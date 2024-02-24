import subprocess
import json
import sys

def run_ping_scan(target):
    command = ["nmap", "-sP", target]
    
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.stderr:
            print("Error executing nmap:", result.stderr)
            sys.exit(1)
        return result.stdout
    except Exception as e:
        print("An error occurred while executing nmap:", str(e))
        sys.exit(1)

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
            host_info = {"host": host, "status": "up", "type": "Unknown"}
        elif "MAC Address:" in line:
            parts = line.split(" ", 3)
            if len(parts) > 2:
                host_info["mac"] = parts[2]
                host_info["type"] = parts[3].strip("()") if len(parts) == 4 else "Unknown"
    if host_info:
        scan_results["hosts"].append(host_info)
    
    return scan_results
10
def save_results(scan_results, filename='PingScanResult.json'): #Save result to a JSON file
    with open(filename, 'w') as file:
        json.dump(scan_results, file, indent=4)
    print(f"Scan results saved to {filename}")

if __name__ == "__main__":
    target = input("Enter the target IP or subnet (e.g., '192.168.1.0/24'): ")
    output = run_ping_scan(target)
    scan_results = parse_nmap_output(output)
    save_results(scan_results)
