class ReceiverProperty:
    def __init__(self, code, receiver_value):
        self.code = code
        self.receiver_value = receiver_value

    def __str__(self):
        return f'Receiver property:  Code: {self.code}  Value: {self.receiver_value}'
