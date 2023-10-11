import unittest
from practicasx import sum_numbers

class testSum(unittest.TestCase):
    def test_sumNumbers_default_args(self):
        """
        Test default args
        """
        self.assertEqual(sum_numbers(), 5050)
        self.assertEqual(sum_numbers(numbers=None), 5050)
        
    
    def test_sumNumbers_variuos_inputs(self):
        self.assertEqual(sum_numbers(range(1,11)), 55)
        self.assertEqual(sum_numbers([1, 2, 3]), 6)
        self.assertEqual(sum_numbers((1, 2, 3)), 6)
        self.assertEqual(sum_numbers([]), 0)
        
         


if __name__ == '__main__':
    unittest.main()