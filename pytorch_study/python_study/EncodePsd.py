import itertools
import zipfile
import pyzipper




file_name = "交通银行账单.zip"


# 利用zipfile来解压zip文件

# 封装解压方法
def uncompress(fileName, passWord):
    try:
        with zipfile.ZipFile(file=fileName) as zFile:
            zFile.extractall("./",pwd=passWord.encode("utf-8"))
            return True
    except:
        return False


# 假如你知道你的密码是a～z和0～9的组合，
# chars = "abcdefghijklmnopqrstuvwxyz0123456789"
chars = "0123456789"
# 利用itertools生成4位随机组合的密码候选集
for e in itertools.permutations(chars,6):
    # 直接输出是一个元组，随机pwd: ('9', '7', 'a', 'j')
    # print("随机pwd:",e)
    password = "".join(e)
    result = uncompress(file_name, password) # bool
    if result:
        print("解压成功",password)
    else:
        print("解压失败",password)
    

