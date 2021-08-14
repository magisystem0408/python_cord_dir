import string
import random
from Crypto.Cipher import AES

print(AES.block_size)
print(string.ascii_letters)

key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
# 暗号化するときは、16文字でないとだめ

iv = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)

print(key, iv)


# 暗号化させるときは必ず16文字でないといけない。
# ここで16文字になるように整形してあげる必要がある。

plaintext = "gfaj:@pfja@sdpofjua@w0tgha[]foj"
cipher = AES.new(key, AES.MODE_CBC, iv)

padding_length = AES.block_size - len(plaintext) % AES.block_size
plaintext += chr(padding_length) *padding_length


# 暗号化させある
cipher_text =cipher.encrypt(plaintext)

print()
print(cipher_text)


# 複合化してあげる
cipher2 =AES.new(key,AES.MODE_CBC,iv)
decrypted_text =cipher2.decrypt(cipher_text)


print(decrypted_text[:decrypted_text[-1]])


