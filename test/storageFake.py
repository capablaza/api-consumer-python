from main.service.storage import Storage
from main.service.paymentRequest import PaymentRequest
from main.service.sale import Sale
from main.service.creditCard import CreditCard


class StorageFake(Storage):

    def __init__(self):
        self.paymentRequests = []

    def save(self, request):
        self.paymentRequests.append(request)

    def find(self, sale):
        for request in self.paymentRequests:
            if request.sale == sale:
                return request
        return PaymentRequest(Sale(), CreditCard("", 0))
