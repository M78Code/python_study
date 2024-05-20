# 创建一个函数，让这个函数可以自动的帮助我们生产函数
def begin_end(old):
    """
        用来对其他函数进行扩展，使其他函数可以在执行前打印开始执行，执行后打印执行结束

        参数：
            old 要扩展的函数对象
    """

    # 创建一个新函数
    def new_function(*args, **kwargs):
        # 调用被扩展的函数
        result = old(*args, **kwargs)
        # 返回函数的执行结果
        return result

    # 返回新函数
    return new_function


# f = begin_end()
# f2 = begin_end()
# print(f)
# print(f2)


def say():
    print("hello world")


@begin_end
def my_say():
    print("my say")


my_say()
