import pytest
import test_calculation
import os
"""
conftest
osの種類によって処理する実行内容を変えていきたいときにどうするか？
必ず、conftest.pyを作ってあげる必要がある


コマンド実行れい
pytest test_calculation.py --os-name=mac -s

--os-name=macなどconftestで設定した内容の引数を繋げる

-sで実行内容が見れるようになる

"""


class TestCal(object):

    @classmethod
    def set_up_class(cls):
        cls.cal = test_calculation.Cal()
        cls.test_file_name='test.txt'

    #第二引数にrequestをつけるのはpytestの決まりごと
    def test_add_num_and_double(self, request):
        os_name = request.config.getoption('--os-name')

        print(os_name)

        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')

        # assert self.cal.add_num_and_double(1, 1) == 4


    # temdirを作ってくれる
    def test_add_num_and_double(self, tmpdir):
        print(tmpdir)
        assert self.cal.add_num_and_double(1,1) ==4


    def test_save(self,tmpdir):
        self.cal.save(tmpdir,self.test_file_name)
        test_file_path =os.path.join(
            tmpdir,self.test_file_name
        )
        assert os.path.exists(test_file_path) is True


    def test_add_num_double(self,csv_file):
        print(csv_file)
        assert self.cal.add_num_and_double(1,1) ==4