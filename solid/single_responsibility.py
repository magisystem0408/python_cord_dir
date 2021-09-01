#単一責任の法則
# 同じ役割を入れるということ

# ユーザー情報を保持する役割を持つ

class Userinfo:

    def __init__(self,name,age,phone_number):
        self.name =name
        self.age =age
        self.phone_number =phone_number

    def __str__(self):
        return "{}{}{}".format(
            self.name,self.age,self.phone_number
        )

#クラスを分ける
class FikeManager:
    @staticmethod
    def write_to_file(obj,filename):
        with open(filename,mode="w")as fh:
            fh.write(str(obj))

userinfo =Userinfo('Taro',21,'00-000-000')
print(str(userinfo))


FikeManager.write_to_file(userinfo,'tmp.txt')




