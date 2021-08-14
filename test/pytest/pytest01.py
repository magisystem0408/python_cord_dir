import pytest
import test_calculation


# test_ と書くとtestと認識されるようになる

def test_add_num_and_double():
    cal = test_calculation.Cal()
    assert cal.add_num_and_double(1, 1) == 4


# classで書く場合
class TestCal(object):
    def test_add_num_and_double(self):
        cal = test_calculation.Cal()
        assert cal.add_num_and_double(1, 1) == 4


    # 例外テストを書く場合
    def test_add_num_and_double(self):
        with pytest.raises(ValueError):
            cal =test_calculation.Cal()
            cal.add_num_and_double('1','1')