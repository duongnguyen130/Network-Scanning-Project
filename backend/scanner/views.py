from django.http import JsonResponse
from .ping_scan import run_ping_scan, parse_nmap_output, save_ping_results as save_ping
from .detailed_scan import run_detailed_scan
import json

def ping_scan_view(request):
    output = run_ping_scan("10.15.149.0/24")  # Adjust subnet as needed
    result = parse_nmap_output(output)
    save_ping(result)
    return JsonResponse(result)

def detailed_scan_view(request):
    result = run_detailed_scan()  # no ip_list needed, it reads from file
    return JsonResponse(result)

