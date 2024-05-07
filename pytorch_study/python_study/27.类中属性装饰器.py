class Person:
    def __init__(self, name):
        self._name = name

    # property装饰器，用来将一个get方法，转换为对象的属性
    # 添加property装饰器后，就可以像调用属性一样使用get方法
    # 使用property装饰的方法，必须和属性名是一样的
    # getter是必须的
    @property
    def name(self):
        print('get方法执行了～～～')
        return self._name

    # setter方法的装饰器：@属性名.setter
    @name.setter
    def name(self, name):
        print('setter方法执行了～～～')
        self._name = name


p = Person('Kotlin')
# print(p.name)
p.name = 'Java'
# print(p.name())
print(p.name)
