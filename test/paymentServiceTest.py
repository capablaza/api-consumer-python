import unittest

from main.service.sale import Sale
from main.service.paymentService import PaymentService
from main.service.creditCard import CreditCard
from main.service.paymentResponse import PaymentResponse
from .loggerdummy import LoggerDummy
from .storageDummy import StorageDummy
from .emailSenderDummy import EmailSenderDummy
from .paymentRestClientStub import PaymentRestClientStub
from .emailSenderMock import EmailSenderMock
from .emailSenderSpy import EmailSenderSpy
from .storageFake import StorageFake

class PaymentServiceTest(unittest.TestCase):

    def setUp(self):
        self.logger = LoggerDummy()
        self.storage = StorageDummy()
        self.emailSender = EmailSenderDummy()
        self.sale = Sale()
        self.creditCard = CreditCard('visa', 987923)

    def test_givenSaleAndCreditCardWhenBothAreCorrectThenPaymentRequestIsFill(self):

        paymentService = PaymentService(
            self.logger, self.emailSender, self.storage)
        paymentRequest = paymentService.createPaymentRequest(
            self.sale, self.creditCard)

        self.assertTrue(paymentRequest.isFill())

    def test_givenPaymentRequestWhenIsValidThenResponseCodeIs200(self):
        paymentService = PaymentService(
            self.logger, self.emailSender, self.storage)
        paymentRequest = paymentService.createPaymentRequest(
            self.sale, self.creditCard)

        restClient = PaymentRestClientStub(200)

        paymentResponse = paymentService.sendPayment(
            paymentRequest, restClient)

        self.assertEqual(paymentResponse.code, PaymentResponse.OK)

    def test_givenPaymentRequestWhenResponseIsErrorThenSendEmail(self):
        emailSender = EmailSenderMock()

        paymentService = PaymentService(self.logger, emailSender, self.storage)
        paymentRequest = paymentService.createPaymentRequest(
            self.sale, self.creditCard)

        restClient = PaymentRestClientStub(500)

        paymentResponse = paymentService.sendPayment(
            paymentRequest, restClient)

        self.assertEqual(paymentResponse.code, PaymentResponse.ERROR)
        emailSender.expected(paymentRequest)
        self.assertTrue(emailSender.verify())

    def test_givenPaymentRequestWhenResponseIsErrorThenSendEmailOnce(self):
        emailSender = EmailSenderSpy()

        paymentService = PaymentService(self.logger, emailSender, self.storage)
        paymentRequest = paymentService.createPaymentRequest(self.sale, self.creditCard)

        restClient = PaymentRestClientStub(500)

        paymentResponse = paymentService.sendPayment(paymentRequest, restClient)

        self.assertEqual(paymentResponse.code, PaymentResponse.ERROR)

        self.assertEqual(1, emailSender.timesCalled())

    def test_givenPaymentRequestWhenIsWrongThenStorageHaveRequestSaved(self):
        
        storage = StorageFake()        

        paymentService = PaymentService(self.logger, self.emailSender, storage)
        paymentRequest = paymentService.createPaymentRequest(self.sale, self.creditCard)

        restClient = PaymentRestClientStub(500)

        paymentResponse = paymentService.sendPayment(paymentRequest, restClient)

        self.assertEqual(paymentResponse.code, PaymentResponse.ERROR)
        requestFromStorage = storage.find(self.sale)

        self.assertEqual(requestFromStorage, paymentRequest)

if __name__ == '__main__':
    unittest.main()
