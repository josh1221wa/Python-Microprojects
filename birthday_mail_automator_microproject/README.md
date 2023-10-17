# Microproject - Birthday Mail Automator

This documentation explains a Python script that automates sending birthday greetings via email to people in a CSV file. It uses email templates and sends personalized birthday wishes based on the current date and the data in the CSV file.

## Purpose

The purpose of this script is to send birthday emails to people whose birthdays match the current date, as specified in a CSV file. It reads the CSV file, checks for birthday matches, and sends personalized birthday emails.

## Dependencies

To run this script, you need the following dependencies:

- `csv`: This Python module is used to read data from a CSV file.
- `datetime`: The `datetime` module is used to get the current date and time.
- `smtplib`: This library is used for sending emails via SMTP.
- `random`: The `random` module is used to select a random letter template.
- `confidential`: This module contains your confidential email address and password for sending emails.

## Usage

1. The script starts by importing the necessary modules and reading your email address and password from the `confidential` module.
2. It gets the current date using the `datetime` module.
3. It establishes an SMTP connection to a Gmail server using your email address and password for sending emails.
4. It reads data from a CSV file called "birthdays.csv," which should contain information about people's names, email addresses, birthdates, and other details.
5. For each entry in the CSV file (excluding the header), the script checks if the birthdate matches the current date.
6. If there is a match, it selects a random letter template from the "letter_templates" directory and replaces the "[NAME]" placeholder with the recipient's name.
7. It sends a personalized birthday email to the recipient with a subject and message from the letter template.
8. The script prints the subject and message for each email sent.

## Security Considerations

Storing your email password in the script may not be secure. It's recommended to use secure methods for storing sensitive information, such as environment variables or configuration files.

## Email Templates

The script uses email templates stored in the "letter_templates" directory. You can customize these templates or add more templates to provide different birthday messages.

## License

This script is provided for educational and personal use. Please respect any licensing and usage restrictions associated with the dependencies and data used in the script.

Enjoy sending personalized birthday wishes to your friends and family with this Python automation tool!
