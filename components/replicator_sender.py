from constants.datasets import DATASET
from models.collection_description import CollectionDescription


class ReplicatorSender:
    buffer = [
        CollectionDescription(0, DATASET[1], []),
        CollectionDescription(1, DATASET[2], []),
        CollectionDescription(2, DATASET[3], []),
        CollectionDescription(3, DATASET[4], [])
    ]

    # From Writer
    @staticmethod
    def ReceiveData(data):
        ReplicatorSender.__SaveData(data)

    @staticmethod
    def __SaveData(data):
        dataset = ReplicatorSender.__IdentifyDataset(data)
        for cd in ReplicatorSender.buffer:
            if dataset == cd.dataset:
                ReplicatorSender.buffer[cd.id].historical_collection.append(data)
                return

    @staticmethod
    def __IdentifyDataset(data):
        for dataset in DATASET.values():
            if data.code in dataset:
                return dataset

    # To Replicator Receiver
    @staticmethod
    def SendData():
        # TODO: Implement
        #  Send data to ReplicatorReceiver in format CollectionDescription
        pass
