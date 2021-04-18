from main.service.emailSender import EmailSender


class EmailSenderMock(EmailSender):

    def __init__(self):
        self.paymentRequests = []
        self.expectedPaymentRequests = []

    def sendEmail(self, paymentRequest):
        self.paymentRequests.append(paymentRequest)

    def expected(self, paymentRequest):
        self.expectedPaymentRequests.append(paymentRequest)

    def verify(self):
        return self.paymentRequests.__len__() == self.expectedPaymentRequests.__len__()
        
