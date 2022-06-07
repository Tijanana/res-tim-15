class Writer:
    def __init__(self):
        self.activity = False

    # To Replicator Sender
    def SendData(self):
        pass

    def SwitchState(self, new_state=None):
        if new_state is None:
            self.activity = not self.activity
        else:
            self.activity = new_state
