import os
import smtplib

from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from email.mime.image import MIMEImage
from dotenv import load_dotenv
load_dotenv()

# Load email configuration from environment variables
PORT = 465
EMAIL_SERVER = os.getenv('email_server')
EMAIL_ADDRESS = os.getenv('email_address')
EMAIL_PASSWORD = os.getenv('email_password')
RESEVER_ADDRESS = os.getenv('reciver_address')

# Create the email message
msg = EmailMessage()
msg['Subject'] = 'About Grab dinner this weekend'
msg['From'] = EMAIL_ADDRESS
msg['To'] = RESEVER_ADDRESS

# Set the email content as HTML
html_content = """
    <html>
    <body>
    <head>
    <style>
  body {
    font-family: Arial, sans-serif;
  }
  h1 {
    color: #333;
  }
  p {
    font-size: 16px;
    color: purple;
  }
</style> 
    </head>
    <h1>Grab Dinner</h1>
    <p>How about grabbing dinner this Saturday?</p>
    <img src="cid:lion.jpg">
    <img src="cid:ethfood1.jpg">
    <img src="cid:ethfood.jpg">
    </body>
    </html>
    """
msg.add_alternative(html_content, subtype='html')

# List of files to attach
files = ['lion.jpg', 'ethfood1.jpg', 'ethfood.jpg']

# Attach each file with appropriate Content-ID (CID)
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_extension = os.path.splitext(file)[1][1:]  # Get the file extension without the dot
        maintype, subtype = 'image', file_extension
        cid = os.path.basename(file)
        
        # Create a new MIMEImage object and attach it
        img = MIMEImage(file_data, maintype=maintype, subtype=subtype)
        img.add_header('Content-ID', f'<{cid}>')
        img.add_header('Content-Disposition', 'inline', filename=cid)
        msg.attach(img)

with smtplib.SMTP_SSL(EMAIL_SERVER, PORT) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
