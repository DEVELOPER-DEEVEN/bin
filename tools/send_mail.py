#!/usr/bin/env python3
import smtplib
import json
import argparse
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

CONFIG_PATH = Path("/home/DEV/OpenClaw/config/mail.json")

def load_config():
    if not CONFIG_PATH.exists():
        print(f"Error: Config file not found at {CONFIG_PATH}")
        sys.exit(1)
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def attach_file(msg: MIMEMultipart, path: Path):
    with open(path, "rb") as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{path.name}"')
    msg.attach(part)


def send_email(to_email, subject, body_text, attachments=None):
    config = load_config()
    
    sender_email = config['sender_email']
    password = config['password']
    smtp_server = config['smtp_server']
    smtp_port = config['smtp_port']

    msg = MIMEMultipart()
    msg['From'] = f"Harvy <{sender_email}>"
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body_text, 'plain'))

    for att in attachments or []:
        path = Path(att)
        if path.exists():
            attach_file(msg, path)
        else:
            print(f"Warning: attachment not found: {path}")

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, to_email, text)
        server.quit()
        print(f"Email sent successfully to {to_email}")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send an email using configured SMTP.')
    parser.add_argument('--to', required=True, help='Recipient email')
    parser.add_argument('--subject', required=True, help='Email subject')
    parser.add_argument('--body', required=True, help='Email body text (or path to file)')
    parser.add_argument('--attach', action='append', help='File path to attach (can be repeated)')
    
    args = parser.parse_args()
    
    # Check if body is a file path
    body_content = args.body
    if Path(args.body).exists():
         with open(args.body, 'r') as f:
             body_content = f.read()

    success = send_email(args.to, args.subject, body_content, attachments=args.attach)
    if not success:
        sys.exit(1)
