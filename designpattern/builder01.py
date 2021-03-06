from abc import ABC, abstractmethod, abstractproperty


# prodact
class SetMeal:

    @property
    def main_dish(self):
        return self.__main_dish

    @main_dish.setter
    def main_dish(self, main_dish):
        self.__main_dish = main_dish

    @property
    def side_dish(self):
        return self.__side_dish

    @side_dish.setter
    def side_dish(self, side_dish):
        self.__side_dish = side_dish

    def __str__(self):
        return f'メインディッシュ：{self.main_dish},サイドディッシュ{self.side_dish}'


# builderのインターフェース
class SetMealBuilder(ABC):
    # 抽象クラスなので継承先で使用しないといけない

    def __init__(self):
        self._set_meal = SetMeal()

    @abstractproperty
    def product(self):
        pass

    @abstractmethod
    def build_main_dish(self):
        pass

    @abstractmethod
    def build_side_dish(self):
        pass


class SannmaSetBuilder(SetMealBuilder):
    def __init__(self):
        super().__init__()

    @property
    def product(self):
        return self._set_meal

    def build_main_dish(self):
        self._set_meal.main_dish = 'さんま'

    def build_side_dish(self):
        self._set_meal.side_dish = 'お味噌汁'


class PastaSetBuilder(SetMealBuilder):
    def __init__(self):
        super().__init__()

    @property
    def product(self):
        return self._set_meal

    def build_main_dish(self):
        self._set_meal.main_dish = "パスタ"

    def build_side_dish(self):
        self._set_meal.side_dish = "スープ"


# ディレクターが外部から呼び出すもの


class Director:

    def __init__(self, builder: SetMealBuilder):
        self.__builder = builder

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, builder):
        self.__builder = builder

    def build(self):
        self.builder.build_main_dish()
        self.builder.build_side_dish()
        return self.builder


sanma_builder = SannmaSetBuilder()
pasta_builder = PastaSetBuilder()

director = Director(sanma_builder)
print(director.build().product)
# print(director.builder.product)
"""実行結果：メインディッシュ：さんま,サイドディッシュお味噌汁"""

director.builder = pasta_builder
director.build()
print(director.build().product)
# print(director.builder.product)
