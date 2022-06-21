from components.logger import Logger
from components.replicator_receiver import ReplicatorReceiver
from constants.datasets import DATASET
from models.collection_description import CollectionDescription
from models.receiver_property import ReceiverProperty


class ReplicatorSender:
    buffer = []

    # From Writer
    @staticmethod
    def ReceiveData(data: ReceiverProperty):  # pragma: no cover
        ReplicatorSender.__SaveData(data)
        ReplicatorSender.__SendData()

    @staticmethod
    def __SaveData(data: ReceiverProperty):  # pragma: no cover
        dataset, cd_id = ReplicatorSender.IdentifyDataset(data)
        collection_description = CollectionDescription(cd_id, dataset, [data, ])
        ReplicatorSender.buffer.append(collection_description)

    @staticmethod
    def IdentifyDataset(data: ReceiverProperty):
        try:
            cd_id = 0
            for dataset in DATASET.values():
                if data.code in dataset:
                    return dataset, cd_id
                cd_id += 1
        except:
            return False

    # To Replicator Receiver
    @staticmethod
    def __SendData():  # pragma: no cover
        for cd in ReplicatorSender.buffer:
            ReplicatorReceiver.ReceiveData(cd)
            Logger.LogAction(f"[Replicator Sender] Forwarded dataset {cd.id}")
        ReplicatorSender.buffer.clear()
