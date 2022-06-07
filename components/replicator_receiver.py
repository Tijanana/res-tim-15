from constants.datasets import DATASET
from models.collection_description import CollectionDescription


class ReplicatorReceiver:
    buffer = [
        CollectionDescription(0, DATASET[1], []),
        CollectionDescription(1, DATASET[2], []),
        CollectionDescription(2, DATASET[3], []),
        CollectionDescription(3, DATASET[4], [])
    ]

    # From Replicator Sender
    @staticmethod
    def ReceiveData(collection_description: CollectionDescription):
        for receiver_property in collection_description.historical_collection:
            ReplicatorReceiver.buffer[collection_description.id].historical_collection.append(receiver_property)

    # To available Reader
    @staticmethod
    def SendData():
        # TODO: Implement
        pass
