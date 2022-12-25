import os
import smtplib
import ssl
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()

email_sender = "arielkolomiets@gmail.com"
email_password = os.getenv("EMAIL_PASSWORD")
email_receiver = ""

subject = "test"

body = """
test pyhton sender email
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject

em.set_content(body)

ctx = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
