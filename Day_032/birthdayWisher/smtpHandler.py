import smtplib


class SmtpHandler:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def start_connection(self):
        self.connection = smtplib.SMTP(self.host, self.port)
        self.connection.starttls()
        self.connection.login(self.user, self.password)

    def send_email(self, to_addrs, msg):
        self.start_connection()
        self.connection.sendmail(
            from_addr=self.user, to_addrs=to_addrs, msg=msg)
        self.close_connection()

    def close_connection(self):
        self.connection.close()
