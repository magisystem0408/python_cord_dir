import contextlib

def is_ok_job():
    try:
        print('do something')
        # エラーを発生させる
        raise Exception('errror')
        return True
    except Exception:
        return False

def cleanup():
    print('clean up')

def cleanup2():
    print('cleanup')

# 普通に書いた場合
# try:
#     is_ok =is_ok_job()
#     print('more task')
# finally:
#     #falseが入ってくる
#     if not is_ok:
#         cleanup()

with contextlib.ExitStack() as stack:
    # どんな処理でもcallbackが最後に呼び出されることになる
    #　直しスタックなので最後に呼ばれたやつ順に出される
    stack.callback(cleanup)
    stack.callback(cleanup2)

    # また以下のように書いても実行される
    @stack.callback
    def cleanup3():
        print('clean up3')

    is_ok =is_ok_job()
    print('more task')

    # falseになった場合、最後に呼び出される処理:cleanupがpopされる
    if is_ok:
        stack.pop_all()
