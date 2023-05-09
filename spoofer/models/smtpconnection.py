import smtplib
import traceback
from socket import gaierror
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ..utils import logger

class SMTPConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket  = host + ':' + port
        self.server  = None
        self.sender = None
        self.recipients = None

        self.__connect()
        self.__start_tls()
        self.__eval_server_features()

    def __ehlo(self):
        try:
            self.server.ehlo()
            if not self.server.does_esmtp:
                logger.error('Server tidak mendukung')
                exit(1)
        except smtplib.SMTPHeloError:
            logger.error('Ada kesalahan dengan server.')
            exit(1)

    def __connect(self):
        try:
            logger.info('Menghubungkan ke jasa (' + self.socket + ')...')
            self.server = smtplib.SMTP(self.host, self.port)
        except (gaierror, OSError):
            logger.error('Gagal menghubungkan.')
            exit(1)

    def __start_tls(self):
        self.__ehlo()
        if not self.server.has_extn('starttls'):
            logger.error('Server SMTP tidak mendukung TLS.')
            exit(1)
        else:
            try:
                logger.info('Memulai TLS...')
                self.server.starttls()
            except RuntimeError:
                logger.error('SSL/TLS tidak tersedia untuk juru bahasa Python Anda.')
                exit(1)

    def __eval_server_features(self):
        self.__ehlo()

        if not self.server.has_extn('auth'):
            logger.error('Tipe AUTH tidak terdeteksi.')
            exit(1)

        server_auth_features = self.server.esmtp_features.get('auth').strip().split()
        supported_auth_features = { auth_type for auth_type in {'PLAIN', 'LOGIN'} if auth_type in server_auth_features }

        if not supported_auth_features:
            logger.error('Server tidak mendukung AUTH PLAIN atau AUTH LOGIN.')
            exit(1)

    def login(self, username, password):
        try:
            return self.server.login(username, password)
        except smtplib.SMTPAuthenticationError:
            logger.error('Server tidak menerima kombinasi nama pengguna/sandi.')
            return False
        except smtplib.SMTPNotSupportedError:
            logger.error('Perintah tidak didukung oleh server.')
            exit(1)
        except smtplib.SMTPException:
            logger.error('Menemukan kesalahan selama otentikasi.')
            exit(1)

    def compose_message(self, sender, name, recipients, subject, html):
        self.sender = sender
        self.recipients = recipients

        message = MIMEMultipart('alternative')
        message.set_charset("utf-8")

        message["From"] = name + "<" +  self.sender + ">"
        message['Subject'] = subject
        message["To"] = ', '.join(self.recipients)

        body = MIMEText(html, 'html')
        message.attach(body)
        return message;

    def send_mail(self, message):
        try:
            logger.info('Mengirim Pesan Tolol...')
            self.server.sendmail(self.sender, self.recipients, message.as_string())
            logger.success('Berhasil YA KONTOL..!')
        except smtplib.SMTPException:
            logger.error('GAGAL PEPEK. Kau periksa pengirim, penerima, dan isi pesan')
            logger.error(traceback.format_exc())
            exit(1)
