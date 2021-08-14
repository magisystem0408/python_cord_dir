"""
seleniumはUI系のtestを使用する時に使う
"""

import unittest
import time
from selenium import webdriver

# html情報を送るやつ
from selenium.webdriver.common.by import By

#　key情報を送るやつ
from selenium.webdriver.common.keys import Keys

# 次にクリックしたページがどんな状態になっているかを確認する
from selenium.webdriver.support import expected_conditions as EC

#　クリックした時にどれぐらい待つかを確認する
from selenium.webdriver.support.ui import WebDriverWait


class PythonOrgTest(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_python_org(self):
        self.driver.get('http://www.python.org')

        # titleにPythonという文字が入っているか確認できる
        self.assertIn('Python',self.driver.title)




        self.driver.find_element_by_link_text('Downloads').click()
        # 開いて情報をとってくる
        element =WebDriverWait(self.driver,10).until(
            # これを見つけて帰ってくるまで
            #　状態を見つけて戻ってくる
            EC.presence_of_element_located(
                (By.CLASS_NAME,'widget-title'
            )))

        #　判定をする
        self.assertEqual('Active Python Releases',element.text)


        #　上の練習
        self.driver.find_element_by_link_text('Documentation').click()
        element =WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME,'call-to-action')))

        self.assertEqual('Browse the docs online or download a copy of your own.',element.text)


        # 検索を自動化
        element =self.driver.find_element_by_name('q')
        element.clear()

        element.send_keys('pycon')
        element.send_keys(Keys.RETURN)

        assert 'No results found' not in self.driver.page_source
