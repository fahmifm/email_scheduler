import smtplib


class Util():
    """Utility Class"""
    def __init__(self):
        # email setup
        self.smtpserver = 'smtp.gmail.com:587'
        self.username = 'ff0102236@gmail.com'
        self.password = 'fml12345'

    def sendemail(self, data):
        message = data[1]
        to_addr_list = [data[2]]

        # Build message
        header = 'From: {}\n'.format('Email Scheduler')
        header += 'To: {}\n'.format(','.join(to_addr_list))
        header += 'Subject: {}\n'.format(data[0])
        message = header + message

        # Send email
        server = smtplib.SMTP(self.smtpserver)
        server.starttls()
        server.login(self.username, self.password)
        problems = server.sendmail(
            'ff0102236@gmail.com', to_addr_list, message)
        server.quit()
