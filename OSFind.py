def identify_OS(output):
    """
    Attempts to identify the operating system from nmap output.
    Prioritizes 'OS details', falls back to 'Aggressive OS guesses',
    and finally checks for known device hints like 'iphone'.
    """
    lines = output.splitlines()
    os_info = "Unknown"

    for line in lines:
        lower_line = line.lower()
        if "iphone" in lower_line:
            return "iOS"

        if "os details:" in lower_line:
            parts = line.split(":", 1)
            if len(parts) > 1:
                return parts[1].strip()

        if "aggressive os guesses:" in lower_line:
            parts = line.split(":", 1)
            if len(parts) > 1:
                return parts[1].strip()

    return os_info
