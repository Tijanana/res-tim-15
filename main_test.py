import unittest
from unittest.mock import patch

from main import *


class MainTest(unittest.TestCase):
    @patch(
        'inquirer2.prompt.prompt',
        return_value={'menu': 'Use writer'}
    )
    def test_get_user_input(self, p1):
        self.assertEqual('Use writer', GetUserInput())

    def test_get_active_writer_names_empty(self):
        self.assertEqual([], GetActiveWriterNames())

    def test_get_active_writer_names_full(self):
        AddWriter(Writer(1))
        self.assertEqual(['Writer 1 On'], GetActiveWriterNames())

    def test_identify_writers_empty(self):
        actual = IdentifyWriters(['Writer 100 On'])
        excpected = [None]

        self.assertEqual(excpected, actual)

    def test_identify_writers_full(self):
        w = Writer(1)
        AddWriter(w)

        actual = IdentifyWriters(['Writer 1 On'])
        actual_all = []
        for writer in actual:
            actual_all.append(writer.__str__())

        excpected = ['Writer 1 On']

        self.assertEqual(excpected, actual_all)

    def test_identify_writer_empty(self):
        actual = IdentifyWriter(['Writer 100 On'])
        excpected = None

        self.assertEqual(excpected, actual)

    def test_identify_writer_full(self):
        w = Writer(1)
        AddWriter(w)

        actual = IdentifyWriter('Writer 1 On')
        excpected = w

        self.assertEqual(excpected.__str__(), actual.__str__())

    def test_validate_regex_valid(self):
        self.assertEqual(True, ValidateRegex('2022-06-12', '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'))

    def test_validate_regex_invalid(self):
        self.assertEqual(False, ValidateRegex('wrong input', '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'))

    def test_map_code_to_dataset_valid(self):
        self.assertEqual(1, MapCodeToDataset('CODE_ANALOG'))

    def test_map_code_to_dataset_invalid(self):
        self.assertEqual(None, MapCodeToDataset('wrong input'))

    def test_generate_writer(self):
        self.assertEqual(True, isinstance(GenerateWriter(), Writer))

    @patch(
        'inquirer2.prompt.prompt',
        return_value={'writer': 'Writer 1 On'}
    )
    @patch('main.GetActiveWriterNames', return_value=['Writer 1 On'])
    @patch('main.IdentifyWriter', return_value=Writer(1))
    def test_select_writer_valid(self, p1, p2, p3):
        self.assertEqual(True, isinstance(SelectWriter(), Writer))

    @patch(
        'inquirer2.prompt.prompt',
        return_value={'writer': 'Writer 1 On'}
    )
    @patch('main.GetActiveWriterNames', return_value=[])
    @patch('main.IdentifyWriter', return_value=Writer(1))
    @patch('builtins.print', return_value=None)
    @patch('builtins.input', return_value=None)
    def test_select_writer_invalid(self, p1, p2, p3, p4, p5):
        self.assertEqual(None, SelectWriter())


if __name__ == '__main__':
    unittest.main()
