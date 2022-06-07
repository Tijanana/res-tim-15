from random import randint

from components.reader import Reader
from constants.datasets import DATASET
from models.collection_description import CollectionDescription
from models.delta_cd import DeltaCD


class ReplicatorReceiver:
    buffer = [
        CollectionDescription(0, DATASET[1], []),
        CollectionDescription(1, DATASET[2], []),
        CollectionDescription(2, DATASET[3], []),
        CollectionDescription(3, DATASET[4], [])
    ]
    buffer_contents_send_status = [
        False,
        False,
        False,
        False
    ]
    delta_cd = DeltaCD([], [])

    # From Replicator Sender
    @staticmethod
    def ReceiveData(collection_description: CollectionDescription):
        for receiver_property in collection_description.historical_collection:
            ReplicatorReceiver.buffer[collection_description.id].historical_collection.append(receiver_property)

    # To available Reader
    @staticmethod
    def SendData():
        ReplicatorReceiver.__EvaluateBufferStatus()
        ReplicatorReceiver.__PrepareData()
        ReplicatorReceiver.__SendPreparedData()

    @staticmethod
    def __EvaluateBufferStatus():
        code_1_present = False
        code_2_present = False
        for cd in ReplicatorReceiver.buffer:
            for receiver_property in cd.historical_collection:
                if receiver_property.code == cd.dataset[0]:
                    code_1_present = True
                elif receiver_property.code == cd.dataset[1]:
                    code_2_present = True
            if code_1_present and code_2_present:
                ReplicatorReceiver.buffer_contents_send_status[cd.id] = True
            else:
                ReplicatorReceiver.buffer_contents_send_status[cd.id] = False

    @staticmethod
    def __PrepareData():
        for cd in ReplicatorReceiver.buffer:
            if not ReplicatorReceiver.buffer_contents_send_status[cd.id]:
                continue

            _ = randint(0, 1)
            if _ == 1:
                ReplicatorReceiver.delta_cd.add.append(cd)
            else:
                ReplicatorReceiver.delta_cd.update.append(cd)

    @staticmethod
    def __SendPreparedData():
        if len(ReplicatorReceiver.delta_cd.add) + len(ReplicatorReceiver.delta_cd.update) != 10:
            return

        for cd in ReplicatorReceiver.delta_cd.add:
            Reader.SaveData(cd)
        for cd in ReplicatorReceiver.delta_cd.update:
            Reader.SaveData(cd)
