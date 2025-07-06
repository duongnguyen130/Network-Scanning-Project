import PingScan
import DetailedScan
import sys

def main():
    print("=== Step 1: Running Ping Scan ===")
    try:
        PingScan.pingScan()  
    except Exception as e:
        print(f"[ERROR] Ping Scan failed: {e}")
        sys.exit(1)

    print("\n=== Step 2: Running Detailed Scan ===")
    try:
        DetailedScan.detailedScan()  
    except Exception as e:
        print(f"[ERROR] Detailed Scan failed: {e}")
        sys.exit(1)

    print("\n✅ Network scan complete. Results saved to OSScanResult.json")

if __name__ == "__main__":
    main()
