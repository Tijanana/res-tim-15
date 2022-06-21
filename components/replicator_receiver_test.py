import unittest

from components.replicator_receiver import ReplicatorReceiver
from constants.codes import Code
from models.receiver_property import ReceiverProperty


class ReplicatorReceiverTest(unittest.TestCase):
    def test_evaluate_buffer_status_valid(self):
        ReplicatorReceiver.buffer[0].historical_collection = [
            ReceiverProperty(Code.CODE_ANALOG, 100),
            ReceiverProperty(Code.CODE_DIGITAL, 101)
        ]
        self.assertEqual(True, ReplicatorReceiver.EvaluateBufferStatus())

    def test_evaluate_buffer_status_invalid(self):
        ReplicatorReceiver.buffer[0].historical_collection = [
            ReceiverProperty(Code.CODE_ANALOG, 100),
        ]
        self.assertEqual(False, ReplicatorReceiver.EvaluateBufferStatus())


if __name__ == '__main__':
    unittest.main()
