import contextlib
import os

# ここで存在しないファイルを消そうとする
# 通常で書いた場合
try:
    os.remove('timi.tmp')
except FileNotFoundError:
    pass


# FileNotFoundErrorが出るやつはsuppressされる
with contextlib.suppress(FileNotFoundError):
    os.remove('timi.tmp')