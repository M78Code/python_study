class A(object):
    def test(self):
        print("test---AAA")


class B(object):

    def test(self):
        print("test---BBB")

    def test2(self):
        print('BBB')


# 在Python中是支持多重继承的
#   可以在类名的()后边添加多个类，来实现多重继承
#   多重继承，会使子类同时拥有多个父类，并且会获取到所有父类中的方法
# 在开发中没有特殊的情况，应该尽量避免使用多重继承，因为多重继承会让代码过于复杂
# 如果多个父类中有同名的方法，则会先在第一个父类中寻找，然后找第二个，然后找第三个。。。
#   前边会覆盖后边的
class C(B):
    pass


class D(B, A, ):
    pass


# 类名.__bases__ 这个属性可以用来获取当前类的所有父类
print(C.__bases__)  # (<class '__main__.B'>,)
# 说明返回的是一个元组

result1 = D.__base__
print(result1)  # <class '__main__.A'>

result2 = D.__bases__
print(result2)  # (<class '__main__.A'>, <class '__main__.B'>)

d = D()
d.test()
# d.test2()
