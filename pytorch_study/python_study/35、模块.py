# 模块（module）
# 模块化，将一个完整的程序分解为一个一个的模块
#   通过将模块组合，来搭建出一个完整的程序

# 在python中一个py文件就是一个模块，
# 在一个模块中引入外部模块
# 1 import 模块名（模块名，就是python文件的名字，注意不要py）
# 2 import 模块名 as 模块别名
#   - 在每一个模块内部都有__name__属性，通过这个属性可以获取到模块的名字
#   - __name__属性值为 __main__的模块是模块，一个程序中只会有一个主模块
#       主模块就是我们直接通过 python执行的模块

# import test_module
# import test_module as tm

# 访问模块中的属性
# print(tm.a)
# tmc = tm.TestModuleClass()
# print(tmc.name)


# 也可以只引入模块中的部分内容
# 语法 from 模块名 import 变量,变量....
# from test_module import TestModuleClass
# from test_module import test
# from test_module import TestModuleClass, test
# 引入到模块中所有内容，一般不会使用
# from test_module import *


# 也可以为引入的变量使用别名
# 语法: from 模块 import 变量 as 别名
# from


def test23():
    print("主模块中的Test2")


# test23()


