"""継承とか実行できるものは継承先を実行できるようにする"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def calcurate_area(self):
        return self._width * self._height


class Squre(Rectangle):

    def __init__(self, size):
        self._width = self._height = size

    @Rectangle.width.setter
    def width(self, size):
        self._width = self._height = size

    @Rectangle.height.setter
    def height(self, size):
        self._width = self._height = size


def print_area(obj):
    change_to_width = 10
    change_to_height = 20
    obj.width = change_to_width
    obj.height = change_to_height

    # ここで判定
    if isinstance(obj, Squre):
        change_to_width = change_to_height

    print('予想={},実際={}'.format(
        change_to_height * change_to_width,
        obj.calcurate_area()
    ))


rc = Rectangle(2, 3)
print_area(rc)

# 子要素を継承している
sq = Squre(5)
print_area(sq)
