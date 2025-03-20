import re

def parse_logs(log_file):
    suspicious_events = []
    
    with open(log_file, "r") as file:
        for line in file:
            if "Failed password" in line or "authentication failure" in line:
                ip = extract_ip(line)
                suspicious_events.append((line.strip(), ip))
    
    return suspicious_events

def extract_ip(log_entry):
    match = re.search(r'[0-9]+(?:\.[0-9]+){3}', log_entry)
    return match.group(0) if match else None
