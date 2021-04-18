from main.service.emailSender import EmailSender

class EmailSenderDummy(EmailSender):
    
    def sendEmail(self, request):
        pass
