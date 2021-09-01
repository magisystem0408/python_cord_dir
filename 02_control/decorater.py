# デコレータは処理の共通化をしたい時に使用する

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('*' * 100)
        func(*args, **kwargs)
        print('*' * 100)
        print()

    return wrapper


@my_decorator
def func_a(*args, **kwargs):
    print('func_aを実行')
    print(args)


@my_decorator
def func_b(*args, **kwargs):
    print('func_bを実行します')
    print(args)


func_a(1, 2, 3)
func_b(4, 5, 6)
