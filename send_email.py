import smtplib
import ssl


def send_email(user_email, email_title, raw_message):
    host = "smtp.gmail.com"
    port = 465

    username = "lhanco@gmail.com"
    password = "hjml zoar vzaa aoiu"

    receiver = "lhanco@gmail.com"
    context = ssl.create_default_context()

    message = f"""\
Subject: {email_title}

From: {user_email}

{raw_message}
"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

