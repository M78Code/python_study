# 集合（set）
# 集合中只能存储不可变对象
# 集合中存储的对象是无序（不是按照元素的插入序保存）
# 集合中不能出现重复的元素
# 使用{}来创建集合
from unittest import result

s = {10, 3, 5, 1, 2, 2, 21, 1, 1}
print(s, type(s))

# 使用 set() 函数来创建集合
s = set()  # 空集合

s = set([1, 23, 4, 5, 67, 181, 11, 1, 2, 3])
s = set('hello')
print(s, type(s))

# 使用set()将字典转换为集合时，只会包含字典中的键
s = set({'a': 1, 'b': 2, 'c': 3})
print(s, type(s))

# 创建集合
s = {'a', 'b', 1, 2, 3}
print(s, type(s))

# print(s[1])
print(f'根据索引取值:{list(s)[0]}')

# 使用in和not in 来检查集合中的元素
print('c' in s)
# 使用len()来获取集合中元素的数量
print(len(s))

# add() 向集合中添加元素
s.add('Leon')

# update()将一个集合中的元素添加到当前集合中
s2 = set('hello')
s.update(s2)
print(f"s2 = {s}")

# 在对集合做运算时，不会影响原来的集合，而是返回一个运算结果
# 创建两个集合
s = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

# & 交集运算
result = s & s2  # {3,4,5}
print(f"交集运算的结果: {result}")

# | 并集运算
result = s | s2  # {1, 2, 3, 4, 5, 6, 7}
print('并集运算的结果: ', result)

# - 差集
result = s - s2  # {1, 2}
print('差集运算的结果:', result)

# ^ 异或集  获取只在一个集合中出现的元素
result = s ^ s2  # {1, 2, 6, 7}
print("异或集运算的结果:", result)

# <= 检查一个集合是否是另一个集合的子集
# 如果一个集合中的元素全部都在另一个集合中出现，那么这个集合
#   就是另一个集合的子集
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
result = a <= b  # True
print("检查一个集合是否是另一个集合的子集:", result)

# 如果a集合中的元素全部都在b集合中出现，那么a集合就是b集合的子集，b集合是a集合的直超集
result = {1, 2, 3} <= {1, 2, 3}  # True
print("两个集合是相等:", result)
result = {1, 2, 3, 4, 5} <= {1, 2, 3}  # False
print(result)

# < 检查一个集合是否是另一个集合的真子集
# 如果超集b中含有子集a中所有元素，并且b中还有a中没有的元素，
#   则b就是a的真超集，a是b的真子集
result = {1, 2, 3} < {1, 2, 3}  # False
result = {1, 2, 3} < {1, 2, 3, 4, 5}  # True

# >= 检查一个集合是否是另一个的超集
# >  检查一个集合是否是另一个的真超集
print("result = ", result)
