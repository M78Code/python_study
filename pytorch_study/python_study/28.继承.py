# 继承

# 定义一个类Animal（动物）
#   这个类中需要两个方法：run(), sleep()

class Animal:

    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"一支叫${self.name}的动物在跑")

    def sleep(self):
        print(f"一支叫${self.name}的动物在睡觉")


# 定义一个类Dog（狗）
#   这个类中需要三个方法：run() sleep() bark()
# 如何能主瞎个类来实现全部的功能呢？
#   直接从Animal类中继承它的属性
#    － 继承是面向对象三在特性之一
#    － 通过继承可以使一个类获取到其他类中的属性和方法
#    － 在定义类时，可以在类名后的手中事指定当前类的父类（超类，基类，super）
#         子类（衍生类）可以直接继承父类中的所有的属性和方法

class Dog(Animal):

    def bark(self):
        print("狗在叫")


dog = Dog("Dog")
print(dog.bark())
print(dog.run())
print(dog.sleep())

# 在创建类时，如果省略了父类，则默认父类bject
#   object是所有类的父，所有类都继承bject

# issubclass() 检查一个类是否是另一个类的子类
result1 = issubclass(Animal, Dog)
print(f"result1 = {result1}")

result2 = issubclass(Dog, Animal)
print(f"result2 = {result2}")

# isinstance()用来检查一个对象是否是一个类的实例
#   如果这个类是这个对象的父类，也会返回True
#   所有的对象都是object的实例
result11 = isinstance(dog, Dog)
print(f"result11 = {result11}")

result12 = isinstance(dog, object)
print(f"result12 = {result12}")

print(f"result13 = {isinstance(print, object)}")
