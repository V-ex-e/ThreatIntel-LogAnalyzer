from fpdf import FPDF

class ReportGenerator:
    def __init__(self, filename="threat_report.pdf"):
        self.filename = filename
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def add_title(self, title):
        self.pdf.add_page()
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(200, 10, title, ln=True, align="C")

    def add_text(self, text):
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, text)

    def save(self):
        self.pdf.output(self.filename)

def generate_report(suspicious_logs):
    report = ReportGenerator()
    report.add_title("Threat Intelligence Report")

    for log_entry, ip in suspicious_logs:
        report.add_text(f"🚨 Suspicious Activity: {log_entry}")
        if ip:
            report.add_text(f"  ⚠ Potential Threat IP: {ip}\n")

    report.save()
