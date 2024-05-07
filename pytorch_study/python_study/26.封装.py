# 封装是面向对象的三大特性之一
# 封装指的是隐藏对象中一些不希望被外部所访问到的属性或方法
# 如何隐藏一个对象中的属性？
#   - 将对象的属性名，个性为一个外部不知道的名字
# 如何获取（修改）对象中的属性？
#   - 需要提供一个getter和setter方法使外部可以访问到属性
#   - getter获取对象中的指定属性（get_属性名）
#   - setter用来设置对象的指定属性（set_属性名）
# 使用封装，确定增加了类的定义的复杂程序，但是也确保了数据的安全性

class Dog:
    '''
        表示狗的类
    '''

    def __init__(self, name):
        self.hidden_name = name

    def say_hello(self):
        print('Hello %s!' % self.hidden_name)

    def get_name(self):
        '''
            get_name()用来获取对象的name属性
        '''
        return self.hidden_name

    def set_name(self, name):
        self.hidden_name = name


# 可以为对象的属性使用双下划线开头，__xxx
# 双下划线开头的属性，是对象的隐藏属性，隐藏属性只能在类的内部访问，无法通过对象访问
# 其实隐藏属性只不过是Python自动为属性改了一个名字
#   实际上是将名字修改为了 _类名__属性名 比如 __name -> _Person__name
class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


p = Person('Leon')
print(p.get_name())
print(p._Person__name)
p.set_name('Python')
print(p.get_name())


# 使用__开头的属性，实际上依然可以在外部访问，所以这种方式一般不用
#   一般会将一些私有属性（不希望被外部访问的属性）以_开头
#   一般情况下，使用_开头的属性都是私有属性，没有特殊需要不要修改私有属性
class Student:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


p = Student('Leon study Python')
print(p._name)
