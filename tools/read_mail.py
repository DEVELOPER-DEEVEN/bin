#!/usr/bin/env python3
import imaplib
import email
import json
import argparse
import sys
import os
from email.header import decode_header
from pathlib import Path

CONFIG_PATH = Path("/home/DEV/OpenClaw/config/mail.json")

def load_config():
    if not CONFIG_PATH.exists():
        print(f"Error: Config file not found at {CONFIG_PATH}")
        sys.exit(1)
    with open(CONFIG_PATH, 'r') as f:
        config = json.load(f)
        # Infer IMAP server from SMTP if not present (simple heuristic for Gmail)
        if 'imap_server' not in config:
            if 'gmail.com' in config.get('smtp_server', ''):
                config['imap_server'] = 'imap.gmail.com'
            else:
                # Default fallback
                config['imap_server'] = 'imap.gmail.com'
        return config

def clean_text(text):
    if not text:
        return ""
    return text.strip().replace("\r", "").replace("\n", " ")[:100]

def decode_mime_words(s):
    if not s:
        return ""
    decoded_list = decode_header(s)
    result = []
    for content, encoding in decoded_list:
        if isinstance(content, bytes):
            if encoding:
                try:
                    result.append(content.decode(encoding))
                except LookupError:
                    result.append(content.decode('utf-8', errors='ignore'))
            else:
                result.append(content.decode('utf-8', errors='ignore'))
        elif isinstance(content, str):
            result.append(content)
    return "".join(result)

def get_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get("Content-Disposition"))
            if ctype == "text/plain" and "attachment" not in cdispo:
                try:
                    return part.get_payload(decode=True).decode()
                except:
                    pass
    else:
        try:
            return msg.get_payload(decode=True).decode()
        except:
            pass
    return "[No text body found]"

def cmd_list(args, config):
    try:
        mail = imaplib.IMAP4_SSL(config['imap_server'])
        mail.login(config['sender_email'], config['password'])

        # List all folders
        # status, folders = mail.list()
        # print("Available folders:")
        # for folder in folders:
        #     print(folder.decode())

        mail.select(args.folder)

        search_criteria = []
        if args.unread:
            search_criteria.append("UNREAD")
        
        if args.sender:
            search_criteria.append(f'(FROM "{args.sender}")')
        
        if args.subject:
            search_criteria.append(f'(SUBJECT "{args.subject}")')

        if not search_criteria:
            search_criteria.append("ALL")

        criteria_str = " ".join(search_criteria)
        status, messages = mail.search(None, criteria_str)
        
        if status != "OK":
            print("No messages found.")
            return

        email_ids = messages[0].split()
        total = len(email_ids)
        # Get latest N
        latest_ids = email_ids[-args.limit:]

        print(f"Found {total} messages. Showing last {len(latest_ids)}:")
        print(f"{'ID':<6} | {'DATE':<16} | {'FROM':<30} | {'SUBJECT'}")
        print("-" * 80)

        for eid in reversed(latest_ids):
            try:
                # Fetch headers only
                _, msg_data = mail.fetch(eid, "(RFC822.HEADER)")
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        subject = decode_mime_words(msg["Subject"])
                        sender = decode_mime_words(msg["From"])
                        date = msg["Date"][:16]
                        
                        # Truncate for display
                        sender_short = (sender[:27] + '..') if len(sender) > 27 else sender
                        subject_short = (subject[:60] + '..') if len(subject) > 60 else subject
                        
                        print(f"{eid.decode():<6} | {date:<16} | {sender_short:<30} | {subject_short}")
            except Exception as e:
                print(f"Error reading {eid}: {e}")

        mail.close()
        mail.logout()
    except Exception as e:
        print(f"Connection failed: {e}")

def cmd_read(args, config):
    try:
        mail = imaplib.IMAP4_SSL(config['imap_server'])
        mail.login(config['sender_email'], config['password'])
        mail.select(args.folder)

        _, msg_data = mail.fetch(args.read, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)
        
        print("="*60)
        print(f"From: {decode_mime_words(msg['From'])}")
        print(f"Date: {msg['Date']}")
        print(f"Subject: {decode_mime_words(msg['Subject'])}")
        print("="*60)
        print(get_body(msg))
        print("="*60)

        mail.close()
        mail.logout()
    except Exception as e:
        print(f"Error reading email {args.read}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read emails via IMAP")
    subparsers = parser.add_subparsers(dest='command')

    # List command
    p_list = subparsers.add_parser('list', help='List emails')
    p_list.add_argument('--limit', type=int, default=10, help='Max emails to show')
    p_list.add_argument('--unread', action='store_true', help='Show only unread')
    p_list.add_argument('--sender', help='Filter by sender (e.g. github)')
    p_list.add_argument('--subject', help='Filter by subject')

    # Read command
    p_read = subparsers.add_parser('read', help='Read specific email body')
    p_read.add_argument('read', help='Email ID to read')

    parser.add_argument('--folder', default='INBOX', help='Folder to select')
    args = parser.parse_args()
    cfg = load_config()

    if args.command == 'read':
        cmd_read(args, cfg)
    else:
        # Default to list if no command or 'list'
        cmd_list(args, cfg)
