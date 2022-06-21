import unittest
from unittest.mock import patch, Mock, MagicMock

from components.reader import Reader
from constants.codes import Code
from models.receiver_property import ReceiverProperty

conn = Mock()
curr = Mock()
conn.cursor = MagicMock(return_value=curr)
curr.execute = MagicMock(return_value=None)
conn.close = MagicMock(return_value=None)
curr.close = MagicMock(return_value=None)


class TestReader(unittest.TestCase):
    @patch("reader.Logger.LogAction", return_value=None)
    @patch("mysql.connector.connect", return_value=conn)
    def test_read_last_value_valid(self, p1, p2):
        curr.fetchone = MagicMock(return_value=[(100,)])
        r = Reader(1)
        self.assertEqual((100,), r.ReadLastValue(Code.CODE_ANALOG))

    @patch("reader.Logger.LogAction", return_value=None)
    @patch("mysql.connector.connect", return_value=conn)
    def test_read_last_value_invalid(self, p1, p2):
        curr.fetchone = MagicMock(return_value=None)
        r = Reader(1)
        self.assertEqual(None, r.ReadLastValue(Code.CODE_ANALOG))

    @patch("reader.Logger.LogAction", return_value=None)
    @patch("mysql.connector.connect", return_value=conn)
    def test_read_last_value_exception(self, p1, p2):
        curr.fetchone = MagicMock(side_effect=Exception)
        r = Reader(1)
        self.assertRaises(Exception, r.ReadLastValue(Code.CODE_ANALOG))

    @patch("reader.Logger.LogAction", return_value=None)
    @patch("mysql.connector.connect", return_value=conn)
    def test_save_value_valid(self, p1, p2):
        curr.execute = MagicMock(return_value=None)
        r = Reader(1)
        self.assertEqual(True, r.SaveValue(ReceiverProperty(Code.CODE_ANALOG, 100)))

    @patch("reader.Logger.LogAction", return_value=None)
    @patch("mysql.connector.connect", return_value=conn)
    def test_save_value_invalid(self, p1, p2):
        curr.execute = MagicMock(side_effect=Exception)
        r = Reader(1)
        self.assertEqual(False, r.SaveValue(ReceiverProperty(Code.CODE_ANALOG, 100)))

    @patch("reader.Logger.LogAction", return_value=None)
    @patch("mysql.connector.connect", return_value=conn)
    def test_save_value_exception(self, p1, p2):
        curr.execute = MagicMock(side_effect=Exception)
        r = Reader(1)
        self.assertRaises(Exception, r.SaveValue(ReceiverProperty(Code.CODE_ANALOG, 100)))

    @patch("reader.Logger.LogAction", return_value=None)
    @patch("mysql.connector.connect", return_value=conn)
    def test_get_value_by_interval_valid(self, p1, p2):
        curr.execute = MagicMock(return_value=None)
        curr.fetchall = MagicMock(return_value=[(100,)])
        r = Reader(1)
        self.assertEqual([100], r.GetValuesByInterval('', '', '', '', ''))

    @patch("reader.Logger.LogAction", return_value=None)
    @patch("mysql.connector.connect", return_value=conn)
    def test_get_value_by_interval_invalid(self, p1, p2):
        curr.execute = MagicMock(side_effect=Exception)
        r = Reader(1)
        self.assertEqual(None, r.GetValuesByInterval('', '', '', '', ''))

    @patch("reader.Logger.LogAction", return_value=None)
    @patch("mysql.connector.connect", return_value=conn)
    def test_get_value_by_interval_exception(self, p1, p2):
        curr.execute = MagicMock(side_effect=Exception)
        r = Reader(1)
        self.assertRaises(Exception, r.GetValuesByInterval('', '', '', '', ''))


if __name__ == '__main__':
    unittest.main()
