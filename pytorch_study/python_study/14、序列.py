# 序列（sequence)
#   序列是Python中最基本的一种数据结构
#   数据结构指计算机中数据存储的方式
#   序列用于保存一组有序的数据，所有的数据在序列当中都有一个唯一的位置（索引）
#     并且序列中的数据会按照添加的顺序来分配索引
#   序列的分类:
#       可变序列:   列表（list)
#      不可变序列:  字符串（str），元组（tuple）

stus = ["Java", "Kotlin", "Flutter", "Dart", "Kotlin", "JavaScript", "Kotlin", "Python"]
# 修改列表中的元素
# 直接通过索引来修改元素
stus[0] = 'Go'
print(stus)

# 通过del来删除元素
del stus[5]  # 删除索引为5的元素
print(stus)

# 通过切片来修改列表
# 在给切片进行赋值时，只能使用序列
new_stus = stus[0:5]
# print(new_stus)
print(f"切片4～6结果: {stus[4:6]}")
stus[4:6] = ["Life is short", "you need python."]
print(stus)

# 通过切片来修改列表
# 在给切片进行赋值时，只能使用序列
# stus[0:2] = ['牛魔']
stus[0:0] = ['CSS']  # 向索引为0的位置插入元素

# 以上操作，只适用于可变序列
s = "Koltin"
# s[1] = 'a' 不可变序列，无法通过索引来修改
# 可以通过list() 函数将其他的序列转换为list
s = list(s)
print(s)

# 向列表指定位置插入一个元素
# 参数:
#   1、要插入的位置
#   2、要插入的元素
#   stus.insert(2, '唐僧')

#   extend()
#   使用新的序列来扩展当前序列
#   需要一个序列作为参数，它会将该序列中的元素添加到当前列表中
#   stus.extend(['a', 'b'])

#   clear()
#   清空序列
#   stus.clear()

#   pop()
#   根据索引删除并返回被删除的元素
#   result = stus.pop(2) # 删除索引为2的元素
#   result = stus.pop()  # 删除最后一个
#   print('result =',result)

#   remove()
#   删除指定值的元素，如果相同值的元素有多个，只会删除第一个

#   reverse()
#   用来反转列表
#   stus.reverse()

#   sort()
#   用来对列表中的元素进行排序，默认是升序排列
#   如果需要降序排列，则需要传递一个reverse=True,
stus.sort(reverse=True)  # 是否反转
