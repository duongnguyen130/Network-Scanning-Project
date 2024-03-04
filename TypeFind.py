def identify_type(output):
    lines = output.split("\n")
    device_type = "Unknown"  # Default value if no specific type is identified
    
    for line in lines:
        if "telnet" in line or "23/tcp" in line:  # Detect Switches and Routers
            device_type = "Switch/Router"
            break
        elif "printer" in line.lower():  # Detect printers
            device_type = "Printer"
            break 
        elif "Microsoft Windows" in line:  # Detect Windows OS
            device_type = "Personal Computer"
            break 
        elif "iphone" in line or "Iphone" in line:  # Detect Windows OS
            device_type = "Apple Iphone"
            break 
        elif "jetdirect" in line:  # Detect jetdirect
            device_type = "Jetdirect(Allows computer printers to be directly attached to a local area network)"
            break 
        elif "h323hostcall" in line:  # Detect jetdirect
            device_type = "Camera(Video Conferencing Systems)"
            break 

    return device_type
