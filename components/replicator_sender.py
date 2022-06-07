from components.replicator_receiver import ReplicatorReceiver
from constants.datasets import DATASET
from models.collection_description import CollectionDescription
from models.receiver_property import ReceiverProperty


class ReplicatorSender:
    buffer = []

    # From Writer
    @staticmethod
    def ReceiveData(data: ReceiverProperty):
        ReplicatorSender.__SaveData(data)
        ReplicatorSender.__SendData()

    @staticmethod
    def __SaveData(data: ReceiverProperty):
        dataset, cd_id = ReplicatorSender.__IdentifyDataset(data)
        collection_description = CollectionDescription(cd_id, dataset, [data, ])
        ReplicatorSender.buffer.append(collection_description)

    @staticmethod
    def __IdentifyDataset(data: ReceiverProperty):
        cd_id = 0
        for dataset in DATASET.values():
            if data.code in dataset:
                return dataset, cd_id
            cd_id += 1

    # To Replicator Receiver
    @staticmethod
    def __SendData():
        for cd in ReplicatorSender.buffer:
            ReplicatorReceiver.ReceiveData(cd)
        ReplicatorSender.buffer.clear()
