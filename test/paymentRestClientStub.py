from main.service.paymentRestClient import PaymentRestClient
from main.service.paymentResponse import PaymentResponse

class PaymentRestClientStub(PaymentRestClient):

    def __init__(self, code):
        self.code = code

    def sendPayment(self, request):
        return PaymentResponse(self.code)
