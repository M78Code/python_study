class Animal:
    def __init__(self, name):
        self._name = name

    def run(self):
        print("Animal is running.")

    def sleep(self):
        print("Animal is sleeping.")

    # support getter method
    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, name):
    #     self._name = name


# 父类中的所有方法都会被子类继承，包括特殊方法
class Dog(Animal):

    def bark(self):
        print("汪汪汪")

    def run(self):
        print("Dog running.")


dog = Dog("旺财")
print(dog.name)


class Cat(Animal):

    def __init__(self, name, age):
        # Animal.__init__(self, name)
        # 希望可以直接调用父类的__init__来初始化父类中定义的属性
        # 并且通过super()返回对象调用父类方法时，不需要传递self
        super().__init__(name)
        # self._name = name
        self._age = age

    @property
    def name(self):
        print("我是子类中的getter方法，name")
        return self._name

    @name.setter
    def name(self, name):
        print("我是子类中的setter方法，修改name")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        print("我是子类中的getter方法，age")
        self._age = age


c = Cat(name="007", age=3)
# c.name = '小黑'

print(c.name)
print(c.age)
