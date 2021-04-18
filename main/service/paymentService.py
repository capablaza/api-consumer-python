from .paymentRequest import PaymentRequest
from .paymentResponse import PaymentResponse

class PaymentService:

    def __init__(self, logger, emailSender, storage):
        self.logger = logger
        self.emailSender = emailSender
        self.storage = storage

    def createPaymentRequest(self, sale, creditCard):
        self.logger.append("Creating payment for sale : ")
        return PaymentRequest(sale, creditCard)

    def sendPayment(self, request, restClient):
        self.logger.append("Sending payment .... ")
        paymentResponse = restClient.sendPayment(request)
        self.logger.append("Payment response : " + str(paymentResponse.code))

        if paymentResponse.code == PaymentResponse.ERROR:
            self.emailSender.sendEmail(request)
            self.storage.save(request)

        return paymentResponse
