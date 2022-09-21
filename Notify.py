import smtplib, ssl

class Mail:
    def __init__(self):
        self.port = 570
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "taipm.vn@gmail.com"
        self.password = "P@$$w0rdPMT456"

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        
        for email in emails:
            result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()

mail = Mail()
mails = ["taipm@bidv.com.vn"]
subject = "Test"
content = "Test"

mail.send(mails, subject, content)

# if __name__ == '__main__':
#     mails = input("Enter emails: ").split()
#     subject = input("Enter subject: ")
#     content = input("Enter content: ")

#     mail = Mail()
#     mail.send(mails, subject, content)
