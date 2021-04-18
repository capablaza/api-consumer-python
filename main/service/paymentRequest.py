class PaymentRequest:

    def __init__(self, sale, creditCard):
        self.sale = sale
        self.creditCard = creditCard

    def isFill(self):
        return (self.sale is not None and self.creditCard is not None)
