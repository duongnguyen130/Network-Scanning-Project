def identify_OS(output):
    lines = output.split("\n")
    os_info = "Unknown"
    for line in lines:
        if "iphone" in line.lower():
            return "IOS"
        if "OS details:" in line:
            return line.split(":", 1)[1].strip()
        if "Aggressive OS guesses:" in line:
            return line.split(":", 1)[1].strip()
    return os_info