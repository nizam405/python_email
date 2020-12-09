import os
import smtplib
from email.message import EmailMessage
import imghdr

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['nizamuddin405@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Test Subject'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content('Here you can add plin text.')

with open('email-content.html','r') as content:
    html_content = content.read()

msg.add_alternative(html_content, subtype='html')

files = ['file1.jpg','file2.jpg']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
        file_type = imghdr.what(file_name)

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)