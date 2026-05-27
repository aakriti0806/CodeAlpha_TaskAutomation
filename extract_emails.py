import re
import os

# ---- SETTINGS ----
input_file = "C:/Users/HP/Desktop/PROJECT/CodeAlpha_TaskAutomation/input.txt"          # file to read emails from
output_file = "C:/Users/HP/Desktop/PROJECT/CodeAlpha_TaskAutomation/emails_found.txt"  # file to save emails into
# ------------------

# Check if input file exists
if not os.path.exists(input_file):
    print(f"Error: '{input_file}' not found!")
    print("Please create an 'input.txt' file with some text containing emails.")
    exit()

# Read the input file
with open(input_file, "r") as f:
    content = f.read()

print(f"Reading from: {input_file}")
print("-" * 40)

# Find all email addresses using regex pattern
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, content)

# Remove duplicates while keeping order
unique_emails = list(dict.fromkeys(emails))

if len(unique_emails) == 0:
    print("No emails found in the file!")
else:
    # Save to output file
    with open(output_file, "w") as f:
        f.write("Extracted Email Addresses\n")
        f.write("=" * 30 + "\n")
        for i, email in enumerate(unique_emails, 1):
            f.write(f"{i}. {email}\n")
            print(f"Found: {email}")

    print("-" * 40)
    print(f"\n Done{len(unique_emails)} email(s) saved to '{output_file}'")