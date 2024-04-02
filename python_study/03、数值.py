# 在Python中数值分成了三种:整数，浮点数（小数），复数
# 在python中所有的整数都是int类型
a = 10
b = 20
# 在python中的整数的大小没有限制，可以是一个无限大的整数,默认不能超过4300位
# c = 9999 ** 999
#   ** 表示幂
print(a)
print(b)
# print(c)

# 如果数字的长度过大，可以使用下划线作为分割符
c = 123_456_799 #会自动忽略下划线
print(c)

# d = 0123 10进制的数字不能以0开头
# 其他进制的整数
# 二进制以0B开头，
d = 0b11
d = 0B10
print(d)    # 十进制2

# 八进制 0o开头
d = 0o33
print(d)    # 十进制27

# 十六进制 0x开头
d = 0xff
print(d)    # 十进制255
# 其他进制的整数，只要是数字打印时一定是以十进制的形式显示的

# 也可以通过运算符来对数字进行运算
e = 100
e+3
print(e)

f = 100
f = ++f
print(f)

g = -100
g-3
print(g)

# 浮点数（小数），在Python中所有的小数都是float类型
c = 1.23
c = 4.56
# 对浮点数进行运算时，可能会得到一个不精确的结果
c = 0.1+0.2
print(c)    # 0.30000000000000004







