from main.service.emailSender import EmailSender


class EmailSenderSpy(EmailSender):

    def __init__(self):
        self.paymentRequests = []

    def sendEmail(self, request):
        self.paymentRequests.append(request)

    def timesCalled(self):
        return self.paymentRequests.__len__()
