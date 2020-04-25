
import os,argparse,smtplib,imghdr

from email.message import EmailMessage

# Setup command line
parser = argparse.ArgumentParser()

msg = parser.add_argument_group('message')
msg.add_argument('-s','--subject', help='Email subject', default='Email from ND')
msg.add_argument('-b','--body'   , help='Email body', default='Default Message from ND')
msg.add_argument('-c','--html'   , help='Alternative HTML file as email body')

recipients = parser.add_argument_group('recipients')
recipients.add_argument('-t','--to', help='Email To', default='nazadelucca@gmail.com')

attachments = parser.add_argument_group('attachments')
attachments.add_argument('-i','--images', help='Image list. Comma separated')
attachments.add_argument('-f','--files' , help='File list. Comma separated')

args = parser.parse_args()

# Obtain the data from our Google Account
# https://myaccount.google.com/apppasswords
# Set them to environment variables
EMAIL_ADDR = os.environ.get('EMAIL_USER')
EMAIL_PSWD = os.environ.get('EMAIL_PASSWD')

def main():

    msg = EmailMessage()
    msg['From'] = EMAIL_ADDR
    msg['To'] = get_list(args.to)
    msg['Subject'] = args.subject

    body = args.body
    msg.set_content( body.strip() )

    if args.html:
        with open(args.html,'r') as f:
            html = f.read()
        msg.add_alternative(html, subtype='html')

    if args.images:
        imgs = get_list(args.images)
        for img_file in imgs:
            with open(img_file,'rb') as f:
                file_data = f.read()
                file_name = f.name
                file_type = imghdr.what(f.name)

            msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    if args.files:
        files = get_list(args.files)
        for file in files:
            with open(file,'rb') as f:
                file_data = f.read()
                file_name = f.name

            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDR,EMAIL_PSWD)
        smtp.send_message(msg)

def get_list(str_list):
    return list( map( str.strip, str_list.split(',') ) )

if __name__ == "__main__":
    main()
