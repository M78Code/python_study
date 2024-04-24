def fn():
    def fn2():
        print('方法中返回方法')

    return fn2  # 返回值也可以是一个函数


r = fn()  # 这个函数的执行结果就是它的返回值
print(r)  # <function fn.<locals>.fn2 at 0x10443e820>
print(fn)  # <function fn at 0x10439c280>
print(fn())  # <function fn.<locals>.fn2 at 0x10443ed30>


#   仅有return时，或者不写return，则相当于return None
def fn2():
    return


def fn5():
    return 10


# fn5 和 fn5()的区别
print(fn5)  # fn5是函数对象，打印fn5实际在打印函数对象（即内存地址）
print(fn5())  # fn5()是在调用函数，打印fn5()实际上是在打印fn5()函数的返回值
