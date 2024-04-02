# help()是Python中的内置函数
# 通过help()函数可以查询pyhon中的函数的用法
# 语法: help(函数对象)
#   help(print) # 获取print()函数的使用说明


# 文档字符串(doc str)
# 在定义函数时，可以在函数内部编写文档字符串，文档字符串就是函数的说明
# 当我们编写了文档字符串时，就可以通过help()函数杰查看函数的说明
# 文档字符串非常简单，其实直接在函数的第一行写一个字符串就是文档字符串
def fn(a, b, c):
    """
     这是一个文档字符串的示例
     函数的作用: ...
     参数
    :param a:
    :param b:
    :param c:
    :return:
    """
    return 10


help(fn)


# 也可以指定函数的参数类型
# 传参的时候，仍然是灵活的
def calc_sum(a: int, b: bool, c: str):
    """
    python官方文档建议这样写文档字符串，注释用英文
    这是一个求和的函数
    :param a:
    :param b:
    :param c:
    :return:
    """
    return a + b + c


result = calc_sum(1, 2, 3)
print(result)


def fn2(a: int, b: bool, c: str) -> int:
    return a + b + c


result2 = fn2(38, 9, 10)
print('result2', result2)
