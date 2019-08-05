import unittest

from Unit_7.unit7_programming_assignment import Unit7


class Testing(unittest.TestCase):

    # def test_string(self):
    #     a = 'some'
    #     b = 'some'
    #     self.assertEqual(a, b)
    #
    # def test_boolean(self):
    #     a = True
    #     b = True
    #     self.assertEqual(a, b)

    def test_has_duplicates(self):
        unit_seven = Unit7()
        has_duplicates = unit_seven.has_duplicates('bob')
        self.assertEqual(True, has_duplicates)

    def test_histogram(self):
        unit_seven = Unit7
        histogram = unit_seven.histogram('n')
        number_of_b = histogram.get('b')
        self.assertEqual(True, number_of_b == 0)


if __name__ == '__main__':
    unittest.main()
