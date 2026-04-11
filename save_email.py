#I'll edit this branch
from email_logic import extract_email
import os
import csv

columns = ["sn", "username", "domain","full_email"]
filename = "emails_april.csv"

found_emails = extract_email(input("Paragraph: ").strip())

existing_emails = []
if os.path.isfile(filename):
  with open(filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        existing_emails.append(row["full_email"].lower())

new_to_add = []
for email in found_emails:
  if email in existing_emails:
    print(f"Skipping: {email} Already exists! ")
  else:
    new_to_add.append(email)

if new_to_add:
  file_exists = os.path.isfile(filename)
  start_num = len(existing_emails) + 1

  with open(filename, "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)

    if not file_exists:
      writer.writeheader()

    for i,email in enumerate(new_to_add, start=start_num):
        username_x, domain_x = email.split("@")
        writer.writerow({
          "sn": i,
          "full_email": email,
          "domain": domain_x,
          "username": username_x
        })

  print(f"Recorded {len(new_to_add)} new emails successfully in {filename}!")
else:
  print("No new emails to add!")