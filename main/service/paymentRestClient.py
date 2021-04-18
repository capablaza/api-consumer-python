from abc import abstractmethod

class PaymentRestClient:

    @abstractmethod
    def sendPayment(self, request):
        pass