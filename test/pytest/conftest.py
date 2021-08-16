"""
conftestをやるときこのファイルを必ず作成する
"""
import pytest


# testで記入して閉じる必要がない

@pytest.fixture
def csv_file():
    # return 'csv file!!'
    with open('test.csv','w+') as c:
        yield c
        print("after test")


def pytest_addoption(parser):
    parser.addoption('--os-name',default='linux',help='os name')