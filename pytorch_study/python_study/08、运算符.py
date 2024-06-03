# 算术运算符
# + 加法运算符（如果是两个字符之间进行加法运算，则会进行拼串操作）
# - 减法运算符
# * 乘法运算符（如果将字符串和数字相乘，则会对字符串进行复制操作，将字符串重复指定次数）
# / 除法运算符，运算时结果总会返回一个浮点类型
# // 带除，只会保留计算后的整数位（对浮点数做运算时，结果会返回一个浮点数）
a = 5
b = 5 // 2
print(f"b = {b}")
c = 5.0
d = c // 2
print(f"d = {d}")
e = 5
f = e // 2.0
print(f"f = {f}")

k = 5 // 3
print(f"k = {k}")

# ** 幂运算，求一个值的几次幂 
# % 取模，求两个数相除的余数


# 赋值运算符
# = 可以将等号右侧的值给等号左侧的变量
# +=    a += 5 相当于 a = a+5
# -=    a -= 5 相当于 a = a-5
# *=    a *= 5 相当于 a = a*5
# **=   a **= 5 相当于 a = a ** 5 (a的5次幂)
# /=    a /= 5 相当于 a = a/5
# //=   a //= 5 相当于 a = a//5
# %=    a %= 5 相当于 a = a%5


# 关系运算符
# 关系运算符用来比较两个值之间的关系，总会返回一个布尔值
# 如果关系成立，返回True，否则返回False
# > 比较左侧值是否大于右侧值
# >= 比较左侧值是否大于或等于右侧值
# < 比较左侧值是否小于右侧值
# <= 比较左侧值是否小于或等于右侧值

# == 比较两个对象的值是否相等
# ！= 比较两个对象的值是否不相等
# 注意: 相等和不等比较的是对象的值，而不是id
# is 比较两个对象是否是同一个对象，比较的是对象的id
# is not 比较两个对象是否不是同一个对象，比较的是对象的id

# 在python中可以对两个字符串进行大于（等于）或小于（等于）的运算
# 当字符串进行比较时，实际上比较的是字符串的uniCode编码
# 比较两个字符串的uniCode编码时，是逐位比较
# 利用该特性可以对字符串按照字母顺序进行排序，但对中文意义不大
result = 'a' > 'b'  # False
result = 'c' < 'd'  # True
result = 'ab' > 'b'  # False

a1 = "a"
a2 = str("a")
print(a1 == a2)

# 逻辑运算符
# not 逻辑非，一元运算符
#   not 可以对符号右侧的值进行非运算
#       对于布尔值，非运算会对其进行取后操作，True变False，False变True
#       对于非布尔值，非运算会先将其转换为布尔址，然后再取反
a = True
a = not a  # 对a进行非运算

# and 逻辑与
#   and可以对符号两侧的值进行与运算
#     只有在符号两侧的值都为True时，才会返回True，只要有一个False就返回False
#     与运算是找False
#     Python中的与运算是短路与，如果第一个值为False，则不再看第二个值
result = True and True  # True
result = True and False  # False
result = False and True  # False
result = False and False  # False

# or  逻辑或
#    or 可以对符号两侧的值进行或运算
#    或运算只要有一个为True，就返回True
#    或运算是找True
# print(result)
False or print('你猜我会打印吗？')  # 第一个值为False，继续看第二个，所以打印语句执行
True or print('你猜我会打印吗')  # 第一个为True，不看第二个，所以打印语句不执行

# 非布尔值的与或运算
#   当对非布尔值进行与或运算时，Python会将其当做布尔值运算，最终会返回原值
#    与运算的规则
#       与运算是找False，如果第一个值是False，则不看第二个值
#       如果第一个值是False，则直接返回第一个值，否则返回第二个值
#    或运算的规则
#       或运算是找True的，如果第一个值是True，则不看第二个值
#       如果第一个值是True，则直接返回第一个值，否则返回第二个值
#  True and True
result = 1 and 2  # 2
#  True and False
result = 1 and 0  # 0
#  False and True
result = 0 and 1  # 0
#  False and Fasle
result = 0 and None  # 0

# True or True
result = 1 or 2  # 1
# True or False
result = 1 or 0  # 1
# False or True
result = 0 or 1  # 1
# False or False
result = 0 or None  # None
print(result)

# 条件运算符（三目运算符）
# 语法: 语句1 if 条件表达式 else 语句2
# 执行流程:
#       条件运算符在执行时，会先对条件表达式求值判断
#       如果判断结果为True，则执行语句1，并返回执行结果
#       如果判断结果为False，则执行语句，并返回执行结果
# print('Python') if False else print('Kotlin')
a = 40
b = 20
c = 10
# 通过条件运算符获取三个值中的最大值
max1 = a if a > b else b
max1 = max1 if max1 > c else c
print(f"最大值1 = {max1}")
# 整合成一个
max2 = a if (a > b and a > c) else (b if b > c else c)
print(f"最大值2 = {max2}")

# 逻辑运行符（补充）
# 逻辑运算符可以连着使用
result = 1 < 2 < 3  # 相当于1<2 and 2 < 3
result = 10 < 20 > 15
