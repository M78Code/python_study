# 可以在模块中定义变量，在模块中定义的变量，在引入模块后，就可以使用
a = 10
b = 20

# 添加了_下划线的变量，只能在模块内部访问，在通过import *引入时，不会引入_开头的变量
_c = 30


# 可以在模块中定义函数，同样可以通过模块访问到
def test():
    print("module's test")


def test2():
    print("this is module's test2")


# 也可以定义类
# class TestModuleClass(object):
#     def __init__(self):
#         self.name = "模块类中的方法"

# 编写测试代码，这部分代码，只要当前文件作为主模块的时候才需要执行
#   检查当前模块是否是主模块
if __name__ == '__main__':
    test()
    test2()
