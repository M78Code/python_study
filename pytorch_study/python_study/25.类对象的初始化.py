# 创建对象的流程
# p1 = Person()的运行流程
#   1.创建一个变量
#   2.在内存中创建一个新对象
#   3.__init__(self)方法执行
#   4.将对象的id赋值给变量
# 类的基本结构
class ClassName([object]):  # 父类没有可省略
    # 公共的属性...

    # 对象的初始化方法
    def __init__(self, ):
        pass

    # 其他的方法
    def func(self, ):
        pass

    def func2(self, ):
        pass


class Person:
    # name = "Python"

    # 在类中可以定义一些特殊方法（魔术方法）
    # 特殊方法都是以__开头，__结尾的方法
    # 特殊方法不需要自己调用，不要尝试去调用特殊方法
    def __init__(self):
        print('我是特殊方法')

    def __insa__(self):
        print('--insa')

    def say_hello(self):
        print("我是普通方法")
        pass


p = Person()
p.say_hello()
p.__insa__()
