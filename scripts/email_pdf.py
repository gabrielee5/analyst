#!/usr/bin/env python3
"""Send a PDF report as an email attachment via Gmail SMTP."""

import argparse
import os
import smtplib
import sys
from email.message import EmailMessage
from pathlib import Path

from dotenv import load_dotenv

# Load .env from project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

DEFAULT_RECIPIENT = os.getenv("EMAIL_RECIPIENT", "")
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))


def send_pdf(pdf_path: str, subject: str | None = None, recipient: str | None = None):
    """Send a PDF file as an email attachment."""
    pdf = Path(pdf_path).resolve()
    if not pdf.exists():
        print(f"Error: {pdf} not found", file=sys.stderr)
        sys.exit(1)

    to = recipient or DEFAULT_RECIPIENT
    if not to:
        print("Error: no recipient — set EMAIL_RECIPIENT in .env or pass --to", file=sys.stderr)
        sys.exit(1)

    if not SMTP_USER or not SMTP_PASSWORD:
        print("Error: SMTP_USER and SMTP_PASSWORD must be set in .env", file=sys.stderr)
        sys.exit(1)

    if not subject:
        subject = f"[gabrielefabietti.xyz] {pdf.stem.replace('-', ' ').replace('_', ' ').title()}"

    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(
        f"Your gabrielefabietti.xyz research report is ready.\n\n"
        f"Find the PDF attached: {pdf.name}\n\n"
        f"— gabrielefabietti.xyz Research Workstation"
    )

    pdf_data = pdf.read_bytes()
    msg.add_attachment(pdf_data, maintype="application", subtype="pdf", filename=pdf.name)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)

    print(f"📧 PDF emailed to {to}")


def main():
    parser = argparse.ArgumentParser(description="Email a PDF report")
    parser.add_argument("pdf_file", help="Path to the PDF file to send")
    parser.add_argument("--subject", default=None, help="Email subject line")
    parser.add_argument("--to", default=None, help="Recipient email (overrides .env)")
    args = parser.parse_args()
    send_pdf(args.pdf_file, args.subject, args.to)


if __name__ == "__main__":
    main()
