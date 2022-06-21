import time
from random import randint

from components.logger import Logger
from constants.datasets import DATASET
from constants.readers import readers
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
    terminate = False

    # From Replicator Sender
    @staticmethod
    def ReceiveData(collection_description: CollectionDescription):  # pragma: no cover
        for receiver_property in collection_description.historical_collection:
            ReplicatorReceiver.buffer[collection_description.id].historical_collection.append(receiver_property)

    # To available Reader
    @staticmethod
    def SendData():  # pragma: no cover
        while True and not ReplicatorReceiver.terminate:
            time.sleep(2)
            there_is_ready_data = ReplicatorReceiver.EvaluateBufferStatus()
            if there_is_ready_data:
                Logger.LogAction(f"[Info]: There is data ready to be saved")
            ReplicatorReceiver.__PrepareData()
            ReplicatorReceiver.__SendPreparedData()

    @staticmethod
    def EvaluateBufferStatus():
        there_is_ready_data = False
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
                there_is_ready_data = True
            else:
                ReplicatorReceiver.buffer_contents_send_status[cd.id] = False
        return there_is_ready_data

    @staticmethod
    def __PrepareData():  # pragma: no cover
        for cd in ReplicatorReceiver.buffer:
            if not ReplicatorReceiver.buffer_contents_send_status[cd.id]:
                continue

            _ = randint(0, 1)
            if _ == 1:
                ReplicatorReceiver.delta_cd.add.append(cd)
            else:
                ReplicatorReceiver.delta_cd.update.append(cd)

    @staticmethod
    def __SendPreparedData():  # pragma: no cover
        if len(ReplicatorReceiver.delta_cd.add) + len(ReplicatorReceiver.delta_cd.update) < 10:
            return

        for cd in ReplicatorReceiver.delta_cd.add:
            reader = readers[cd.id + 1]
            reader.SaveData(cd)
            Logger.LogAction(f"[Replicator Receiver] Forwarded dataset {cd.id}")
            ReplicatorReceiver.delta_cd.add.clear()
        for cd in ReplicatorReceiver.delta_cd.update:
            reader = readers[cd.id + 1]
            reader.SaveData(cd)
            Logger.LogAction(f"[Replicator Receiver] Forwarded dataset {cd.id}")
            ReplicatorReceiver.delta_cd.update.clear()
