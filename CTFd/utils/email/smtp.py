import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from socket import timeout

from CTFd.utils import get_app_config, get_config


def get_smtp(host, port, username=None, password=None, TLS=None, SSL=None, auth=None):
    if SSL is None:
        smtp = smtplib.SMTP(host, port, timeout=3)
    else:
        smtp = smtplib.SMTP_SSL(host, port, timeout=3)

    if TLS:
        smtp.starttls()

    if auth:
        smtp.login(username, password)
    return smtp


def sendmail(addr, text, subject):
    ctf_name = get_config("ctf_name")
    mailfrom_addr = get_config("mailfrom_addr") or get_app_config("MAILFROM_ADDR")
    mailfrom_addr = formataddr((ctf_name, mailfrom_addr))

    data = {
        "host": get_config("mail_server") or get_app_config("MAIL_SERVER"),
        "port": int(get_config("mail_port") or get_app_config("MAIL_PORT")),
    }
    gmail_user = 'clubscrtrsrch@gmail.com'
    gmail_password = 'efedvhzcntyohyyu'
    sent_from = 'SRC CLUB'
    to = [addr]
    message = 'Subject: {}\n\n{}'.format(subject, text)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, message)
    server.close()