import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_phishing_email(sender_email, recipient_email, smtp_server, smtp_port, smtp_user, smtp_password):
    print("\n[!] WARNING: This script is for educational purposes only. Please use it only in an authorized environment for ethical testing and security awareness.")
    print("[!] Unauthorized use of this code is illegal and unethical. Proceed with caution.\n")

    try:
        subject = "Important Update: Immediate Action Required"
        body = "Click the link below to reset your password:\n\nhttp://malicious-link.com"
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        
        print("\n[+] Phishing email sent successfully (for educational purposes only).")
        
    except Exception as e:
        print(f"[!] An error occurred while sending the email: {e}")

sender_email = "attacker@example.com"
recipient_email = "victim@example.com"
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_user = "attacker@example.com"
smtp_password = "your_password"

send_phishing_email(sender_email, recipient_email, smtp_server, smtp_port, smtp_user, smtp_password)
