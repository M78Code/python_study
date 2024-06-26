# 函数也是一个对象（function）
#   对象是内存中专门用来存储数据的一场区域
#   函数可以用来保存一些可执行的代码，并且可以在需要时，对
#       这些语句进行多次的调用
#   创建函数:
#       def 函数名([型参1, 型参2, 型参3, ... , 型参n]):
#           代码块   
#       函数名必须要符合标识符规则
#   

# 定义一个函数
def fn2():
    print("定义的一个函数")


# 定义一个函数，可以用来求任意两个数的和
def sum(a, b):
    return a + b


# fn是函数对象，fn()调用函数
# print是函数对象，print()调用函数
print(fn2(), type(fn2))
result = sum(3, 4)
print("result = ", result)


# 定义一个函数
# 定义型参时，可以为型参指定默认值
# 指定了默认值后，如果用户传递了参数则默认值没有任何作用
def fn(a=5, b=10, c=20):
    return a + b + c
    # pass


# 实参的传递方式
# 位置参数
# 位置参数就是将对应位置的实参复制给对应位置的型参
fn(1, 2, 3)

# 关键字参数
# 关键字参数，可以不按照型参定义的顺序去传递，而直接根据参数名去传递参数
fn(b=1, c=2, a=3)

# 关键字参数
# 关键字参数，可以不按照型参定义的顺序去传递，而直接根据参数名去传递参数
fn(b=1, c=2, a=3)


# 关键字参数
def fn2(a):
    print('a = ', a)


# 函数在调用时，解析器不会检查实参的类型
# 实参可以传递任意类型的对象
b = 123
b = True
b = 'None'
b = [1, 2, 3]


# fn2(b)
# fn2(fn())

def fn4(a):
    # 在函数中对型参进行重新赋值，不会影响其他的变量
    # a = 20

    # a是一个列表，尝试修改列表中的元素
    # 如果型参执行的是一个对象，当我们通过型参去修改对象时
    # 会影响到所有指向该对象的变量
    a[0] = 30
    print('a =', a, id(a))


c = 10
c = [1, 2, 3]
# print('c =', c, id(c))
fn4(c)
#   希望a和c是独立的
# fn4(c.copy())  # 方法一，通过copy
# fn4(c[:])  # 方法二，通过切片
print('第二次 c =', c, id(c))


# 不定长的参数
# 定义一个函数，可以求任意个数字的和

# 在定义函数时，可以在型参前边加上一个*，这样这个型参将会获取到所有的实参
# 它会将所有的实参保存到一个元组中

# *a会接收所有的位置实参，并且会将这些实参统一保存到一个元组中
def calc_sum(*args):
    su = 0
    for e in args:
        su += e
    return su


# def calc_arr([*a]):


arr = [1, 2, 3, 4, 5, 6, 7, 8, 10]
result = calc_sum(1, 2, 5, 5, 8, 9, 10)
print('result = ', result)


# fn(1,2,3,4,5)
# 带星号的型参只能有一个
# 带星号的参数，可以和其他参数配合使用
# 第一个参数给a，第二个参数给b，剩下的都保存到c的元组中
def fn_c(a, b, *c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)


def fn_c2(a, *b, c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)


# fn_c(1, 2, 3, 4, 5)

# 可变参数不是必须写在最后，但是注意，带*的参数后的所有参数，必须以关键字参数的形式传递
fn_c2(1, 2, 3, 4, c=5)


# 所有的位置参数都给a，b和c必须使用关键字参数
def fn_c3(*a, b, c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)


# 如果在型参的开头直接写一个*，则所有的参数必须以关键字的形式传递
def fn_c4(*, a, b, c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)


fn_c4(a=33, b=44, c=5)


# *型参只能接收位置参数，而不能接收关键字参数
# def fn_c5(*a):
#     print('a = ', a)
#
# fn_c5(b=1, )

# **型参可以接收其他的关键字参数，它会将这些参数统一保存一个字典中
#   字典的key是参数的名字，字典的value是参数的值
# ** 型参只能有一个，并且必须写在所有参数的最后
def fn_c6(**args):
    print('args = ', args)


fn_c6(a=1, b=2, c=3333)


def fn_c7(b, c, **a):
    print('a = ', a, type(a))
    print('b = ', b, type(b))
    print('c = ', c, type(c))


fn_c7(b=1, d=2, c=3, e=10, f=20)


def fn_c8(a, b, c):
    print('a = ', a, type(a))
    print('b = ', b, type(b))
    print('c = ', c, type(c))


# 创建一个元组
t = (10, 20, 30)
# 传递实参时，也可以在序列类型的参数前添加星号，这样他会自动将序列中的元素依次作为参数传递
# 这里要求序列中元素的个数必须和型参的个数一致
fn_c8(*t)

# 创建一个字典
d = {'a': 100, 'b': 200, 'c': 300}
fn_c8(**d)
