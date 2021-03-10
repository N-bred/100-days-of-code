import smtplib


class SmtpHandler:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.connection = None

    def start_connection(self):
        self.connection = smtplib.SMTP(self.host, self.port)
        self.smtp.starttls()
        self.connection.login(self.user, self.password)

    def send_message(self, message, to_addrs):
        self.start_connection()
        self.smtp.send_message(message, from_addr=self.user, to_addrs=to_addrs)
        self.end_connection()

    def end_connection(self):
        self.connection.close()
