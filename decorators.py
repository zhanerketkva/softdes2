from message import Message

class MessageDecorator(Message):
    def __init__(self, wrapped_message):
        self._wrapped_message = wrapped_message

    def send(self):
        self._wrapped_message.send()

class EncryptionDecorator(MessageDecorator):
    def send(self):
        encrypted_content = self._encrypt(self._wrapped_message._content)
        print(f"Sending encrypted message: {encrypted_content}")

    def _encrypt(self, content):
        return content[::-1]
