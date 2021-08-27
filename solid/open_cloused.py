# 開放閉鎖の原則
from abc import ABCMeta, abstractmethod


# ソースコードを変更するのではなく追加して修正していく

class UserInfo:
    def __init__(self, user_name, job_name, nationality):
        self.user_name = user_name
        self.job_name = job_name
        self.nationality = nationality

    def __str__(self):
        return '{}{}{}'.format(
            self.user_name, self.job_name, self.nationality
        )


# class UserInfoFilter:
#     @staticmethod
#     def filter_users_job(users, job_name):
#         for user in users:
#             if user.job_name == job_name:
#                 yield user
#
#     @staticmethod
#     def filter_users_nationality(users, nationality):
#         for user in users:
#             if user.nationality == nationality:
#                 yield user
#
#     # jobとnationalityで絞り込まないといけない時、新しく処理をする
#     @staticmethod
#     def filter_users_job_and_nationality(users,job_name,nationality):


# 抽象クラス
class Comparetion(metaclass=ABCMeta):
    @abstractmethod
    def is_equal(self, other):
        pass


class Filter(metaclass=ABCMeta):
    @abstractmethod
    def filter(self, comparetion, item):
        pass


class JobNameComparetion(Comparetion):
    def __init__(self, job_name):
        self.job_name = job_name

    def is_equal(self, other):
        return self.job_name == other.job_name


class NationalityComparation(Comparetion):
    def __init__(self, nationality):
        self.nationality = nationality

    def is_equal(self, other):
        return self.nationality == other.nationality


class UserInfoFilter(Filter):
    def filter(self, comparetion, items):
        for item in items:
            if comparetion.is_equal(item):
                yield item





taro = UserInfo('taro', 'salary man', 'Japan')
jiro = UserInfo('jiro', 'police man', 'japan')
john = UserInfo('john', 'salary man', 'USA')

user_list = [taro, jiro, john]

salary_man_comparetion =JobNameComparetion('salary man')

user_info_filter=UserInfoFilter()

for user in user_info_filter.filter(salary_man_comparetion,user_list):
    print(user)


# for man in UserInfoFilter.filter_users_job(user_list, 'police man'):
#     print(man)
# for man in UserInfoFilter.filter_users_nationality(user_list, 'Japan'):
#     print(man)
