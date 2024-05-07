# 创建一个函数，可以用来求任意数的阶乘

# 阶乘
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


# 递归是解决问题的一种方式，它和循环很像
# 它的整体思想是，将一个大问题分解为一个个小问题，直到问题无法分解时，再
#   去解决问题
#  递归式函数的两个要件
#   1. 基线条件
#       - 问题可以被分解为最小问题，当满足基线条件时，递归就不再执行了
#   2. 递归条件
#       - 将问题继续分解的条件
#   递归和循环类似，基本是可以互相代替
#       循环编写起来比较容易，阅读起来稍难
#       递归编写起来难，但是方便阅读

# 递归
def recursion(n):
    if n == 1:
        # 1的阶乘就是1，直接返回1
        return 1
    # 递归条件
    return n * recursion(n - 1)


a = recursion(10)
print(a)


# 检查一个字符串是否是回文
#   检查 abcdefgedcba是否是回文
#   检查 bcdefgedcb是否是回文
#   检查 cdefgfedc是否是回文
#   检查 defgfed是否是回文
#   检查 efgfe是否是回文
#   检查 fgf是否是回文
#   检查 g是否是回文
def hui_wen(s):
    '''
    该函数用来检查指定的字符串是否回文字符串，如果是返回True，否则False

    参数:
        s:就是要检查的字符串
    '''
    # 基线条件
    if len(s) < 2:
        # 字符串的长度小于2，则字符串一定是回文
        return True
    elif s[0] != s[-1]:
        # 第一个字符和最后一个字符不相待，不是回文字符串
        return False
    # 递归条件
    return hui_wen(s[1:-1])  # 切片，从1开始，表示包含1，所以基线条件没有了


#                            -1结束，不包含结束位置


def hui_wen2(s):
    '''
    该函数用来检查指定的字符串是否回文字符串，如果是返回True，否则False

    参数:
        s:就是要检查的字符串
    '''
    # 基线条件
    if len(s) < 2:
        # 字符串的长度小于2，则字符串一定是回文
        return True
    # 递归条件
    return s[0] == s[-1] and hui_wen(s[1:-1])  # 切片，从1开始，表示包含1，所以基线条件没有了
#                            -1结束，不包含结束位置
