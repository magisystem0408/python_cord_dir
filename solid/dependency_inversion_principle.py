"""
逆依存性逆転の法則
ソフトウェア間のモジュール間の依存関係を切り離すための方法
"""

# NG例
# class Book:
#     def __init__(self,content):
#         self.content = content
#
# class Formatter:
#     # 継承させる
#     def format(self,book:Book):
#         return book.content
#
#
# class Printer:
#     def print(self,book:Book):
#         formatter =Formatter()
#         formatter_book =formatter.format(book)
#         print(formatter_book)
#
# book =Book('My Book')
# printer=Printer()
# printer.print(book)

from abc import ABCMeta, abstractmethod, abstractproperty


# IはinterfaceのIで具体的な処理の形を書かない

class IBook(metaclass=ABCMeta):

    # プロパティはgetterを抽象先で持たないといけない
    @abstractproperty
    def content(self):
        pass


class Book(IBook):
    def __init__(self, content):
        self._content = content

    @property
    def content(self):
        return self._content


class EBook(IBook):
    def __init__(self, content):
        self._content = content

    @property
    def content(self):
        return 'E' + self.content


class IFormatter(metaclass=ABCMeta):

    @abstractmethod
    def format(self, i_book: IBook):
        pass


class HtmlFormatter(IFormatter):

    def format(self, i_book: IBook):
        return '<h1>' + i_book.content + '</h1>'


class XmlFormatter(IFormatter):
    def format(self, i_book: IBook):
        return '<xml>' + i_book.content + '</xml>'


class Printer:
    # これは継承前がabstructだから、排除する
    def __init__(self, i_formatter: IFormatter):
        self._i_formatter = i_formatter

    def print(self, i_book: IBook):
        formatted_book = self._i_formatter.format(i_book)
        print(formatted_book)


book = Book('My Book')
html_formatter = HtmlFormatter()
html_printer = Printer(html_formatter)
html_printer.print(book)

# 基本拡張がしやすくなりやすくなる
xml_formatter = XmlFormatter()
xml_printer = Printer(xml_formatter)
xml_printer.print(book)

ebook = EBook('My EBook')
xml_printer.print(ebook)
