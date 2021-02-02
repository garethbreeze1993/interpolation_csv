import unittest
from helpers import get_interpolate_value, get_new_csv_structure


class HelpersTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.overall_list = [['37.454012', '95.071431', '73.199394', '59.865848', 'nan'],
                             ['15.599452', '5.808361', '86.617615', '60.111501', '70.807258'],
                             ['2.058449', '96.990985', 'nan', '21.233911', '18.182497'],
                             ['nan', '30.424224', '52.475643', '43.194502', '29.122914'],
                             ['61.185289', '13.949386', '29.214465', 'nan', '45.606998']]

    def test_get_interpolate_value_middle_value(self):
        returned_val = get_interpolate_value(coordinates=[2, 2], overall_list=self.overall_list)
        self.assertEqual(64.3295385, returned_val)

    def test_get_interpolate_value_end_value(self):
        returned_val = get_interpolate_value(coordinates=[3, 0], overall_list=self.overall_list)
        rounded_return_val = round(returned_val, 6)
        self.assertEqual(31.222654, rounded_return_val)

    def test_get_new_csv_structure(self):
        expected_structure = [['37.454012', '95.071431', '73.199394', '59.865848', 65.33655300000001],
                              ['15.599452', '5.808361', '86.617615', '60.111501', '70.807258'],
                              ['2.058449', '96.990985', 64.3295385, '21.233911', '18.182497'],
                              [31.222654000000002, '30.424224', '52.475643', '43.194502', '29.122914'],
                              ['61.185289', '13.949386', '29.214465', 39.338655, '45.606998']]
        self.assertEqual(expected_structure, get_new_csv_structure(overall_list=self.overall_list))


if __name__ == '__main__':
    unittest.main()
