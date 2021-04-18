from abc import abstractmethod

class EmailSender:

    @abstractmethod
    def sendEmail(request):
        pass