import requests
import config

API_URL = "https://api.abuseipdb.com/api/v2/check"

def check_ip_threat(ip):
    headers = {
        "Key": config.ABUSE_IPDB_API_KEY,
        "Accept": "application/json"
    }
    
    response = requests.get(f"{API_URL}?ipAddress={ip}&verbose", headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("abuseConfidenceScore", 0)
    
    return None
