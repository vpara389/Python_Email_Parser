import re

def main():
    emails = extract_email(input("Paragraph: ").strip())
    if emails:
        print("\nEmails found:")
        for email in emails:
            print(email)
    else:
        print("No emails found")

def extract_email(paragraph):
    words = paragraph.split()
    found_emails = []

    for word in words:
        if match := re.search(r"[a-z0-9]+(?:[-.@_a-z0-9])*@[a-z]+\.[a-z]+", word, re.IGNORECASE):
            found_emails.append(match.group().lower())
            
    return found_emails
      

if __name__ == "__main__":
    main()