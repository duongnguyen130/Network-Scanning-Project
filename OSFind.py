def identify_OS(output):
    os_info = "Unknown"
    lines = output.split("\n")
    for line in lines:
        if "OS details:" in line:
            os_info = line.split(":")[1].strip()
            break
        if "Aggressive OS guesses:" in line:
            os_info = line.split(":")[1].strip()
            break
        if "iphone:" in line:
            os_info = "IOS"
            break
    return os_info