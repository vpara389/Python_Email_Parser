# Python Email Parser & CSV Recorder

## Description
A Python utility that extracts email addresses from a block of text and saves them into a structured CSV file. The program intelligently skips duplicates by checking the existing records in the database before writing new entries.

## Features
* **RegEx Extraction:** Uses sophisticated Regular Expressions to identify valid email patterns within paragraphs.
* **Duplicate Prevention:** Checks `emails_april.csv` to ensure no email is recorded twice.
* **Automated Formatting:** Automatically splits emails into `username` and `domain` components for better data organization.
* **Sequential Indexing:** Maintains a Serial Number (`sn`) that continues from the last entry in the file.

## File Structure
* `email_logic.py`: Contains the `extract_email` function using the `re` module.
* `main.py`: The primary script that handles user input, duplicate checking, and CSV writing.
* `emails_april.csv`: The output file where data is stored (created automatically on first run).

## Technical Implementation
### RegEx Breakdown
The parser uses the following pattern to catch emails:
`[a-z0-9]+(?:[-.@_a-z0-9])*@[a-z]+\.[a-z]+`
* It supports alphanumeric characters, dots, hyphens, and underscores.
* It utilizes `re.IGNORECASE` to ensure all variations are captured.

### CSV Schema
| Column | Description |
| :--- | :--- |
| **sn** | Sequential Serial Number |
| **username** | Everything before the @ |
| **domain** | Everything after the @ |
| **full_email** | The complete email address (lowercase) |

## How to Use
1.  Run the main script:
    ```bash
    python main.py
    ```
2.  Paste a paragraph containing one or more email addresses when prompted.
3.  The script will notify you of which emails were added and which were skipped.

## Future Roadmap
* Support for parsing bulk `.txt` or `.eml` files directly.
* Validation check to ensure the domain actually exists.