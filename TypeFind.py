def identify_type(output):
    """
    Identifies the device type from nmap scan output.
    Returns a string like "Printer", "Switch/Router", "Personal Computer", etc.
    """
    lines = output.splitlines()
    device_type = "Unknown"

    for line in lines:
        lower_line = line.lower()

        if "telnet" in lower_line or "23/tcp" in lower_line:
            return "Switch/Router"
        elif "printer" in lower_line:
            return "Printer"
        elif "microsoft windows" in lower_line:
            return "Personal Computer"
        elif "iphone" in lower_line:
            return "Apple iPhone"
        elif "jetdirect" in lower_line:
            return "Jetdirect (LAN-connected printer)"
        elif "h323hostcall" in lower_line:
            return "Camera (Video Conferencing System)"

    return device_type
