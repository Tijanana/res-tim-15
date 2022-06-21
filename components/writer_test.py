import unittest

from writer import Writer


class WriterTest(unittest.TestCase):
    def test_validate_value_valid(self):
        self.assertEqual(True, Writer.ValidateValue('1'))

    def test_validate_value_invalid(self):
        self.assertEqual(False, Writer.ValidateValue('0'))

    def test_validate_value_exception_1(self):
        self.assertEqual(False, Writer.ValidateValue('wrong input'))

    def test_validate_value_exception_2(self):
        self.assertRaises(Exception, Writer.ValidateValue('wrong input'))

    def test_switch_state_switch(self):
        w = Writer(1)
        before_state = w.activity
        w.SwitchState()
        after_state = w.activity

        actual = after_state
        expected = not before_state

        self.assertEqual(expected, actual)

    def test_switch_state_set(self):
        w = Writer(1)
        w.activity = False
        w.SwitchState(True)

        self.assertEqual(True, w.activity)


if __name__ == '__main__':
    unittest.main()
