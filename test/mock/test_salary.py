import unittest
from unittest.mock import MagicMock
import salary


class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary.Salary(year=2017)

        # bonus_priceが、中身を実行せずに、仮に1を返してくれるようになる
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)
