
#  Network Scanning Project

This Python-based project automates network scanning using `nmap`. It performs:

1. **Ping Scan** to discover active hosts
2. **Detailed Scan** to detect operating systems and classify device types

---

##  Project Files

```

PingScan.py           # Runs ping scan and saves live hosts
DetailedScan.py       # Detects OS and device type using nmap -O
OSFind.py             # Parses OS info from nmap output
TypeFind.py           # Parses device type from nmap output
network\_scan.py       # Main script that runs both scans
PingScanResult.json   # Output: active IPs from ping scan
OSScanResult.json     # Output: OS and device type per host
README.md             # This documentation

````

---

## How It Works

- **PingScan.py** uses `nmap -sP` to find live hosts
- **DetailedScan.py** uses `nmap -O -Pn` to detect OS
- Results are stored in structured JSON format

---

## Usage

```bash
python network_scan.py
````

1. You’ll be asked to enter a subnet (e.g., `192.168.1.0/24`)
2. The script runs both scans
3. Results are saved in:

   * `PingScanResult.json`
   * `OSScanResult.json`

---

## Requirements

* Python 3.6+
* `nmap` must be installed and in your system PATH

---

## Example Output (OSScanResult.json)

```json
{
  "host": "10.15.149.185",
  "OS": "Microsoft Windows 11 21H2",
  "Device Type": "Personal Computer"
}
```

---

## .gitignore Recommendation

```
# Results
PingScanResult.json
OSScanResult.json

# Python cache
__pycache__/
*.pyc

# Logs and environments
*.log
.env
.venv/
```

---

## 👤 Author

Chi Ngo

---

## License

MIT License – Free to use, modify, and distribute.


