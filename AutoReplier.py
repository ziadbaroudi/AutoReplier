import smtplib
from string import Template
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib
import email


email_address = input("Please Enter your email: ")
email_password = getpass.getpass(prompt="Please Enter your password (It should be " \
                                  "App "
                       "password if you are using 2FA): ", stream=None)

# Will write in senders.txt the emails that it will reply to
# Change "imap-mail.outlook.com" to whatever server you are using
def set_sender(file_name):
    with open(file_name, "w") as senders:
        mail = imaplib.IMAP4_SSL("imap-mail.outlook.com")
        (retcode, capabilities) = mail.login(email_address, email_password)
        mail.list()
        mail.select('inbox')
        (retcode, messages) = mail.search(None, '(UNSEEN)')
        if retcode == 'OK':
            for num in messages[0].split():
                print('Processing ')
                typ, data = mail.fetch(num, '(RFC822)')
                for response_part in data:
                    if isinstance(response_part, tuple):
                        original = email.message_from_bytes(
                            response_part[1])
                        # remove this if you want to reply to all unread emails
                        compare_array = ["<example.email@example.com>",
                                         "<example.email2@example.com>"]
                        if original["From"].split()[-1] in compare_array:
                            senders.write(original["From"])
                            print(original['From'])
                        typ, data = mail.store(num, '+FLAGS', '\\Seen')

set_sender("senders.txt")

# Read email addresses from senders.txt an put them in an array
def get_sender(file_name):
    names = []
    emails = []

    with open(file_name, "r") as senders:
        for sender in senders:
            names.append(sender.split()[0])
            not_formatted_email = sender.split()[-1]
            emails.append(not_formatted_email.replace("<","").replace(">",""))

    return names, emails


def message(file_name):
    with open(file_name, "r") as message:
        message_content = message.read()
    return Template(message_content)


# Change the server according to your email provider

server = smtplib.SMTP(host="smtp-mail.outlook.com", port=587)
server.starttls()
server.login(email_address, email_password)

names, emails = get_sender("senders.txt")
message_temp = message("message.txt")

for name, email in zip(names, emails):
    msg = MIMEMultipart()

    message = message_temp.substitute(NAME = name.title())
    msg['From'] = email_address
    msg['To'] = email
    msg['Subject'] = "RE:Submission"
    msg.attach(MIMEText(message, "plain"))
    server.send_message(msg)
    del msg
