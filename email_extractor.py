# CodeAlpha Task 3: Task Automation with Python Scripts
# Automates: extracting all email addresses from a .txt file
# and saving them to another file.
# Concepts used: os, re, file handling

import os
import re

INPUT_FILE = "input.txt"
OUTPUT_FILE = "emails.txt"

# Pattern that matches most common email addresses
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def extract_emails(text):
    """Return a sorted list of unique email addresses found in text."""
    found = re.findall(EMAIL_PATTERN, text)
    # lowercase + set removes duplicates like Bob@x.com and bob@x.com
    return sorted(set(email.lower() for email in found))


def main():
    print("===================================")
    print("        EMAIL EXTRACTOR")
    print("===================================")

    # Make sure the input file exists before trying to open it
    if not os.path.exists(INPUT_FILE):
        print(f"Error: '{INPUT_FILE}' not found in {os.getcwd()}")
        print("Create it and paste some text containing email addresses.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        text = file.read()

    emails = extract_emails(text)

    if not emails:
        print("No email addresses found.")
        return

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for email in emails:
            file.write(email + "\n")

    print(f"Found {len(emails)} unique email address(es):")
    for email in emails:
        print(f"  - {email}")
    print(f"\nSaved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
