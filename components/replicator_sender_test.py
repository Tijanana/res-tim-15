import unittest

from components.replicator_sender import ReplicatorSender
from constants.codes import Code
from constants.datasets import DATASET
from models.receiver_property import ReceiverProperty


class ReplicatorSenderTest(unittest.TestCase):
    def test_identify_dataset_valid(self):
        self.assertEqual((DATASET[1], 0), ReplicatorSender.IdentifyDataset(ReceiverProperty(Code.CODE_ANALOG, 100)))

    def test_identify_dataset_invalid(self):
        self.assertEqual(False, ReplicatorSender.IdentifyDataset('wrong input'))

    def test_identify_dataset_exception(self):
        self.assertRaises(Exception, ReplicatorSender.IdentifyDataset('wrong input'))


if __name__ == '__main__':
    unittest.main()
