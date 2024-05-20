# 列表Python中的一个对象
# 对象（object)就是内存中专门用来存储数据的一块区域

# 创建列表，通过[]来创建列表
from multiprocessing.dummy import Value

my_list = []  # 创建一个列表
print(my_list, type(my_list))

# 列表存储的数据，称为元素
# 一个列表中可以存储多个元素，也可以在他去列表时，来指定列表中的元素
my_list = [10]  # 创建一个只包含元素的列表

# 当向列表中添加多个元素时，多个元素之间使用逗号(,)隔开
my_list = [1, 2, 50, 11, 3]
print(my_list, len(my_list), type(my_list))
my_list = [1, "", "c"]
print(my_list, len(my_list), type(my_list))

# 通过索引获取列表中的元素
# 语法: my_list[索引] 
# print(my_list[0])

# 获取列表的长度，列表中元素的个数
# len()函数，通过该函数可以获取列表的长度


# 切片
# 切片指从现有列表中，获取一个子列表
# 创建一个列表，一般创建列表时，变量的名字会使用复数
stus = ["Java", "Kotlin", "Flutter", "Dart", "Kotlin", "JavaScript", "Kotlin", "Python"]
print(stus[-1])  # Python

stus2 = ["PHP", "Go"]

# 列表索引可以是负数
# 如果索引是负数，则从后向前获取元素，-1表示倒数第一个，-2表示倒数第二个
# 如果索引是负数，则从后向前获取元素，-1表示倒数第一个，-2表示倒数第二个，以此类推

# 通过切片来获取指定的元素
# 语法: 列表（起始:结束）
# 通过切片获取元素时，会包括起始位置的元素，不会包括结束位置的元素
# 做切片操作时，总会返回一个新的列表，不会影响原来的列表
# 起始和结束位置的索引都可以省略不写

# 如果省略结束位置，则会一直截取到最后
print(stus[1:])

# 如果省略起始位置，则会从第一个元素开始截取
print(stus[:3])

# 如果起始位置和结束位置全部省略，则相当于创建了一个列表的副本
print(stus[:])

stus += stus2
print(stus)

# 语法: 列表[起始:结束:步长]
print(stus[0:5:3])

# + 和 *
# +可以将两个列表拼接为一个列表
my_list = [1, 2, 3] + [4, 5, 6]
print(my_list)
# * 可以将列表重复指定的次数
my_list = [1, 2, 3] * 5
print(my_list)

# in 和 not in
# in用来检查指定元素是否存在于列表中
#   如果存在，返回true，否则返回False
# not in用来检查指定元素是否不存在列表中
#   如果不在，返回True，否则返回False
print('HTML' not in stus)
print('HTML' in stus)

# len()获取列表中的元素的个数

# min() 获取列表中的最小值
# max() 获取列表表中的最大值
arr = [10, 2, 5, 1, 100, 17, 89]
print(min(arr), max(arr))

# 两个方法（method），方法和函数基本上是一样，只不过方法必须通过对象.方法()
# 的形式调用
# xxx.print()方法实际上就是和对象关系紧密的函数
# s.index()获取指定元素在列表中的第一次出现时索引
# index()的第二个参数，表示查找的起始位置，第三个参数，表示查找的结束位置
print(stus.index('Kotlin'))
# 如果要获取列表中没有的元素，会抛出异常
# print(stus.index('HTML')) # ValueError: 'HTML' is not in list

# 统计元素在列表中出现的次数
print(stus.count("Kotlin"))

# 通过while循环来遍历列表
i = 0
while i < len(stus):
    print(stus[i])
    i += 1

# 通过for循环来遍历列表
#   语法:
#     for 变量 in 序列:
#         代码块

for e in stus:
    print(e)

# range()是一个函数，可以用来生成一个自然数的序列
r = range(5)  # 生成一个这样的序列[0,1,2,3,4]
r = range(10)
r = range(0, 10, 2)
r = range(10, 0, -1)

# 该函数需要三个参数
#   1，起始位置（可以省略，默认是0）
#   2，结束位置
#   3，步长（可以省略，默认1）
print(list(r))

# 通过range()可以创建一个执行指定次数的for循环
for e in range(10):
    print(e)

# for e in 0 until 10:

for s in 'Hello World':
    print(s)

# 元组 tuple
# 元组是一个不可变的序列
# 它的操作的方式基本上和列表是一致的
# 一般不改变数据时，就使用元组，其余情况都使用列表

# 创建元组
# 使用()来创建元组
my_tuple = (1, 2, 3, 4, 5)  # 创建了一个空元组
# 元组是不可变对象，不能尝试为元组中的元素重新的赋值
# my_tuple[3] = 9
print(my_tuple)

# 当元组不是空元组时，括号可以省略
# 如果元组不是空元组，它里边至少要有一个，
my_tuple = 10, 20, 30, 40
# my_tuple = 50,

# 元组的解包（解构）
# 解包就是指将元组当中每一个元素都赋值给一个变量
a, b, c, d = my_tuple
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)

a = 100
b = 300
print(a, b)

# 交互a和b的值，这时就可以利用元组的解包
a, b = b, a
print(a, b)

# 在对一个元素进行解包时，变量的数量必须和元组中的元素的数量一致
# 也可以在变量前边添加一个*，这样变量将会获取元组中所有剩余的元素
a, b, *c = my_tuple
a, *b, c = my_tuple
*a, b, c = my_tuple
print("a = ", a)
print("b = ", b)
print("c = ", c)
a, b, *c = [1, 2, 3, 4, 5, 6, 7]
a, b, *c = "hello world"

## 可变对象
#   每个对象中都保存了三个数据:
#       id(标识)
#       type(类型)
#       value(值)

#   列表就是一个可变对象
a = [1, 2, 3]

a[0] = 10  # (改对象)
#   这个操作是在通过变量去修改对象的值
#   这种操作不会改变变量所指向的对象
#   当我们去修改对象时，如果有其他变量也指向了该对象，则修改也会在其他的变量中体现

a = [4, 5, 6]  # (改变量)
#   这个操作是在给变量重新赋值
#   这种操作会改变变量所指定的对象
#   为一个变量重新赋值，不会影响其他的变量


#   ==、！=、is、is not
#   == != 比较的是对象的值是否相等
#   is, is not 比较的是对象的id是否相等（比较两个对象是否同一个对象）

m = [1, 2, 3]
n = [1, 2, 3]
print(m, n)
print("m = ", id(m), m)
print("n = ", id(n), n)
print(m == n)  # m和n的值相等，使用==会返回True（一般用这个就够了）
print(m is b)  # m和n不是同一个对象，内存地址不同，使用is会返回False
