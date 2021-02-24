import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read.text())
email = EmailMessage()
email["from"] = "Awinash Awasthy"
email["to"] = "awinash@outlook.com"
email["subject"] = "you won 1lac rs!!"

email.set_content(html.substitute({"name":"tintin"}),html)

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("awinash@gmail.com","hggfd")
    smtp.send_message()
    print("all good")
    
