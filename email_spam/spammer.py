import smtplib

def func(tup:tuple):
    return tup[0]

class GMAIL():
    def __init__(
        self,
        receiver :str,
        body :str,
        count :int= 1,
        sender :str = None

    ):
        self.sender = sender,
        self.receiver = receiver,
        self.body = body,
        self.count = count,
        self.smtplib = smtplib,

    def send(self):

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo() # Can be omitted
        server.starttls() # Secure the connection
        server.login('<email from messages are being send>','<password of email>')
        if int(self.count[0])>10:
            int(self.count[0]) == 10
        else:
            pass
        for i in range(int(self.count[0])):
            server.sendmail(self.sender[0],self.receiver[0],self.body[0])
        server.quit()
