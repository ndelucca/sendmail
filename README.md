PYMAILER Script

Mailer script for gmail account.

Additional features:
    Send HTML content
    Send images as attachments
    Send any file as attachments

Every list of arguments is indicated as a comma separated list

Version: Python 3.6

For usage:
>>> pymailer.py --help

Examples:

>>> pymailer.py --to mail1@mail.com,mail2@mail.com --subject "Test Email" --body "Test Email Content"

>>> pymailer.py --to mail1@mail.com,mail2@mail.com --subject "Test Email" --html content.html

>>> pymailer.py --to mail1@mail.com --subject "Test Email" --body "Test Email Content" -i image.jpg -f file.pdf
