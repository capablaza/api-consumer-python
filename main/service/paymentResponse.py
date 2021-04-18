class PaymentResponse:

    OK = 200
    ERROR = 500

    def __init__(self, code):
        self.code = code
