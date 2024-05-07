# 多态是面向对象的三大特征之一
# 多态从字面上理解是多种形态
# 狗(狼狗，哈士奇，古牧)
# 一个对象可以以不同的形态去呈现

# 定义两个类
class A:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class B:
    def __init__(self, name):
        self._name = name

    def __len__(self):
        return 100

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class C:
    pass


a = A("Kotlin")
b = B("Java")
c = C()


# 定义一个函数
# 对于say_hello()这个函数来说，只要对象中含有name属性，它就可以作为参数传递
# 这个函数并不会考虑对象的类型，只要有name属性即可
def say_hello(obj):
    print("hello %s" % obj.name)


say_hello(b)

# say_hello(c)

# len()
# 之所以一个对象能通过len()来获取长因为对象中具有一个特殊方法__len__
# l = [1, 2, 3]
# s = "hello"
# print(s.__len__())

print(len(b))


class Animal(object):

    def speak(self):
        print("动物的叫声")
        pass


class Cat(Animal):
    def speak(self):
        print("喵喵")


class Dog(Animal):
    def speak(self):
        print("汪汪")


def speak(obj):
    obj.speak()


class Test:
    def speak(self):
        print("test")


# animal = Animal()
# animal.speak()
# speak(animal)

# kitty = Cat()
# puppy = Dog()
# kitty.speak()
# puppy.speak()

# speak(kitty)
# speak(puppy)

t = Test()
speak(t)
