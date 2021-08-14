"""
ユニットテスト
"""

import unittest

import caluculation

release_name ='lesson'

class CalTest(unittest.TestCase):
# 最初にどんな関数を実行したいかを書いておく
# init関数みたいなやつ

    @classmethod
    def setup_class(cls):
        print("start")
        cls.cal =caluculation.Cal()

    @classmethod
    def teardown_class(cls):
        print("end")
        del cls.cal

    def setup_method(self,method):
        print('method{}'.format(method.__name__))
        # self.cal =caluculation.Cal()

    # 一番最後に呼ばれる
    def teardown_method(self,method):
        print('method{}'.format(method.__name__))
        # del self.cal

# ユニットテストスキップ

# テストスキップしてくれる
#     @unittest.skip('skip!')

    #バージョンとかを書けば、スキップできるようになる
    @unittest.skipIf(release_name=='lesson','skip!!')
    def test_add_num_and_double(self):
        # 第二引数は実行結果の予測
        self.assertEqual(
            self.cal.add_num_and_double(1,1),
            4
        )

# 例外がしっかりと起こるか
    def test_add_num_and_double_raise(self):
        # raiseはwithステートメントで確認する
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1','1')

if __name__ == '__main__':
    unittest.main()