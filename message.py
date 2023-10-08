class Message:
    def send(self):
        pass

class TextMessage(Message):
    def __init__(self, content):
        self._content = content

    def send(self):
        print(f"Sending text message: {self._content}")
