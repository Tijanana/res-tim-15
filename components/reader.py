from mysql import connector


class Reader:
    def __init__(self, processable_dataset):
        self.processable_dataset = processable_dataset

    def SaveData(self, data):
		connection = connector.connect(host='localhost', user='username', passwd='password', database='mysql')
        # TODO: Implement
        #  Saves data received from Replicator Receiver to the Database
        #  Saving is done by the type of dataset
        pass
