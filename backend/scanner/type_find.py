def identify_type(output):
    lines = output.split("\n")
    for line in lines:
        if "telnet" in line or "23/tcp" in line:
            return "Switch/Router"
        elif "printer" in line.lower():
            return "Printer"
        elif "Microsoft Windows" in line:
            return "Personal Computer"
        elif "iphone" in line.lower():
            return "Apple iPhone"
        elif "jetdirect" in line.lower():
            return "Jetdirect (Printer on LAN)"
        elif "h323hostcall" in line.lower():
            return "Camera (Video Conferencing)"
    return "Unknown"