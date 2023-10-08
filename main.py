from message import TextMessage
from decorators import EncryptionDecorator
# Create a base message
base_message = TextMessage("Do the assignment and get a good grade^~^")

# Create a decorator and wrap the base message
encrypted_message = EncryptionDecorator(base_message)

# Send the decorated message
encrypted_message.send()

