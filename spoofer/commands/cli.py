from ..utils import logger, appdescription
from ..models.smtpconnection import SMTPConnection
from ..utils.userinput import get_yes_no


def run(args):
    appdescription.print_description()

    # Connect to SMTP over TLS
    connection = SMTPConnection(args.host, str(args.port))

    # Attempt login
    if not args.noauth:
        success = connection.login(args.username, args.password)
        if success:
            logger.success('Authentication berhasil')
        else:
            exit(1)

    try:
        with open(args.filename) as f:
            message_body = f.read()
    except FileNotFoundError:
        logger.error("File tidak ada: " + args.filename)
        exit(1)

    # Compose MIME message
    message = connection.compose_message(
        args.sender,
        args.name,
        args.recipients,
        args.subject,
        message_body
    )

    if get_yes_no('Woy TOLL mau di kirim sekarang (Y/N)?: ', None):
        connection.send_mail(message)

