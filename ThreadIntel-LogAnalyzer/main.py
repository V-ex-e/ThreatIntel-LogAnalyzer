import log_parser
import threat_check
import report

LOG_FILE_PATH = "logs/syslog"

if __name__ == "__main__":
    suspicious_logs = log_parser.parse_logs(LOG_FILE_PATH)
    
    for entry, ip in suspicious_logs:
        if ip:
            score = threat_check.check_ip_threat(ip)
            print(f"[ALERT] {ip} has a threat score of {score}")

    report.generate_report(suspicious_logs)
    print("🚀 Report generated: threat_report.pdf")
