def identify_OS(output):
    lines = output.split("\n")
    os_info = "Unknown"
    for line in lines:
        if "iphone" in line:
            os_info = "IOS"
            break
        if "OS details:" in line:
            os_info = line.split(":")[1].strip()
            break
        elif "Aggressive OS guesses:" in line:
            os_info = line.split(":")[1].strip()
            break
    return os_info