a = int(10)  # 创建一个int类的实例
b = str('hello')  # 创建一个str类的实例


# 定义一个简单的类
# 使用class关键字来定义类，语法和函数很像

# class 类名([父类]):
#   代码块

class MyClass(object):
    job = "Student"
    age = 28


print(MyClass)

mc = MyClass()  # 使用类来创建对象
print(mc.age)
print(mc.job)


# isinstance()用来检查一个对象是否是一个类的实例
def check():
    return isinstance(mc, MyClass)


result = check()
print(result)


class MyClass2:
    name = "swk"

    # 在类中也可以定义函数，类中定义的函数，被称为方法
    # 这些方法可以通过该类的所有实例来访问
    def say(self):
        # 在方法中不能直接访问类中的属性
        print(f'hello i am $s {self.name}')


mc2 = MyClass2()
# 这是通过MyClass2这个类创建的对象，是一个空对象
# 可以向对象中添加变量，对象中的变量称为属性
# 语法：对象.属性名 = 属性值
mc2.name = 'Python'
mc2.age = 20

# 调用方法，对象.方法名()
# 方法调用和函数调用的区别
# 如果是函数调用，则调用时传几个参数，就会有几个实参
# 方法调用，必须传递一个参数，所以方法中至少要定义一个形参

# 注意：
# 方法调用时，第一个参数由解析器自动传递，所以定义方法时，至少要定义一个形参
# 第一个参数，就是调用方法的对象本身
# 一般都会将这个参数命名为self

# 类对象和实例对象中都可以保存属性（方法）
# - 如果这个属性（方法）是所有的实例共享的，则应该将其保存到类对象中
# - 如果这个属性（方法）是某个实例独有，则应该保存到实例对象中
