import contextlib
# contextDecorator

class tag(contextlib.ContextDecorator):
    def __init__(self,name):
        self.name =name
        self.start_tag='<{}>'.format(name)
        self.end_tag ='</{}>'.format(name)

    # 一番最初に入ってくるとき
    def __enter__(self):
        print(self.start_tag)

    # 最後に呼び出される
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.end_tag)

with tag('h2'):
    print('test')