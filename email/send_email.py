import os
import smtplib
import imghdr
from email.message import  EmailMessage
from email.utils import formataddr
from pathlib import Path 

from dotenv import load_dotenv 
load_dotenv()

PORT = 465
EMAIL_SERVER = os.getenv('email_server')
EMAIL_ADDRESS = os.getenv('email_address')
EMAIL_PASSWORD= os.getenv('email_password')
RESEVER_ADDRESS = os.getenv('reciver_address')

msg = EmailMessage()
msg['Subject'] = 'About Grab dinner this weekend'
msg['From'] = EMAIL_ADDRESS
msg['To'] = RESEVER_ADDRESS
msg.set_content('how about Grabbing diner this saturday')

files = ['lion.jpg','ethfood1.jpg','ethfood.jpg']

for file in files:

    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
with smtplib.SMTP_SSL(EMAIL_SERVER, PORT) as smtp:
 

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)

