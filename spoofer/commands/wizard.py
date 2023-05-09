from colorama import Fore
from getpass import getpass
from ..utils import logger, appdescription
from ..utils.userinput import prompt, get_required, get_optional, get_yes_no
from ..models.smtpconnection import SMTPConnection


def run(args):
    appdescription.print_description()

    host = get_required('SMTP host: ')
    port = None;

    while not port:
        try:
            port = int(get_required('SMTP port: '))
            if port < 0 or port > 65535:
                logger.error('jarak SMTP port sampai (0-65535)')
                port = None
        except ValueError:
            logger.error('Port SMTP harus berupa angka')
            port = None

    # Connect to SMTP over TLS
    connection = SMTPConnection(host, str(port))

    # Attempt login
    if not get_yes_no("Nonaktifkan autentikasi (Y/N)?: ", 'n'):
        success = False
        while not success:
            success = connection.login(
                get_required('Username: '),
                getpass()
            )
        logger.success('Authentication berhasil')

    sender = get_required('Alamat pengirim: ')
    sender_name = get_required('Nama pengirim: ');

    recipients = [get_required('Email tujuan: ')]
    if get_yes_no('Penerima tambahan (Y/N)?: ', 'n'):
        recipient = True;
        while recipient:
            recipient = get_optional('Email penerima: ', None)
            if recipient:
                recipients.append(recipient)

    subject = get_required('Subject line: ')

    html = ''
    if get_yes_no('Isi pesan dalam file (Y/N)?: ', 'n'):
        filename = get_required('NamaFile: ')
        with open(filename) as f:
            html = f.read()
    else:
        logger.info('Masukkan HTML baris demi baris')
        logger.info('Untuk menghentikan, tekan CTRL+D (*nix) atau CTRL-Z (win) pada baris *kosong*')
        while True:
            try:
                line = prompt('>| ', Fore.LIGHTBLACK_EX)
                html += line + '\n'
            except EOFError:
                logger.success('Badan HTML yang diambil')
                break

    # Compose MIME message
    message = connection.compose_message(
        sender,
        sender_name,
        recipients,
        subject,
        html
    )

    if get_yes_no('Woy TOLL mau di kirim skrng (Y/N)?: ', None):
        connection.send_mail(message)
