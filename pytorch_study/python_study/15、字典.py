# 字典（dict）
#   字典属于一种新的数据结构，称为映射（mapping）
#   字典的作用和列表类似，都是用来存储对象的容器
#   列表存储数据的性能很好，但是查询数据的性能很差

# 使用{}来创建字典
from email.policy import default
from os import name

d = {}  # 创建了一个空字典
# 创建一个保护有数据的字典
# 语法:
#   {key: value, key:value}
#   字典的值可以是任意对象
#   字典的键可以是任意不可变对象（int，str，bool，tuple ...）
d = {'name': '孙悟空', 'age': 18, 'gender': '男', 'name': '孙悟空2'}
print(d, type(d))

#  使用dict()函数来创建字典
# 每一个参数都是一个键值对，参数名就是键，参数值就是值（这种方式创建的字典，key都是字符串）
e = dict(name='Kotlin', age='7', gender='Google')
print(e, type(e))

#  也可以将一个包含有双值子序列的序列转换为字典
#  双值序列，序列只有两个值，[1,2] ('a',3) 'ab'
#  子序列，如果序列中的元素也是序列，那么称这个元素为子序列
[(1, 2), (3, 5)]
d = dict([('name', 'Google'), ('age', 40)])
print(d, type(d))

# len() 获取字典中键值对的个数
# in    检查字典中是否包含指定的键
# not in 检查字典中否不包含指定的键

# 通过[]来获取值时，如果键不存在，会抛出异常KeyError
# get(key[, default]) 该方法用来根据键来获取字典中的值
#   如果获取的键在字典中不存在，会返回None
#   也可以指定一个默认值，来作为第二个参数，这样获取不到值的将会返回默认值
print(d.get('name'))
# print(d.get("kkk"))

# setdefault(key[, default]) 可以用来向字典中添加key-value
#   如果key已经存在于字典中，则返回key的值，不会对字典做任何操作
#   如果key不存在，则向字典中添加这个key，
e['address'] = 'Sun'
print(e)
result = e.setdefault('address', '默认值')
print(result)

# update([other])
# 将其他的字典中的key-value添加到当前字典中
# 如果有重复的key，则后边的会替换到当前的
d = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5, 'f': 6, 'a': 7}
d.update(d2)
print(d)

# print(d)
# 删除，可以使用del 来删除字典中的key-value
del d['a']

# popitem()
# 随机删除字典中的一个键值对，一般都会删除最后一个键值对
#   删除之后，它会将删除的key-value作为返回值返回
#   返回的是一个元组，元组中有两个元素，第一个元素是删除的key，第二个是删除的value
# d.popitem()
# result = d.popitem()

# pop(key[,default])
# 根据key删除字典中的key-value
# 会将被删除的value返回！
# 如果删除不存在的key，会抛出异常
#   如果指定了默认值，再删除不存在的key时，不会报错，而是直接返回默认值
result = d.pop('d')
result = d.pop('z', '这是z的默认值')

print('result = ', result)
print(d)

# clear()用来清空字典

# copy() 该方法用于对字典进行浅复制
#        复制以后的对象，和原对象是独立，修改一个不会影响另一个
#   注意，浅复制会简单复制对象内部的值，如果值也是一个可变对象，这个可变对象
#       不会被复制


#  遍历字典
# keys()    该方法会返回字典的所有的key
j = {'name': 'Java', 'age': 25, 'gender': 'Oracle'}
print(j.keys())
# 通过遍历keys()来获取所有的键
for e in j.keys():
    print(f"{e}:{j[e]}---{j.get(e)}")

# values()  
#   该方法会返回一个序列，序列中保存有字典的左右的值
for v in j.values():
    print(v)

# items()
# 该方法会返回字典中所有的项
# 它会返回一个序列，

# items()
# 该方法会返回字典中所有的项
# 它会返回一个序列，序列中包含有双值子序列
# 双值分别是，字典中的key和value
for k, v in j.items():
    print(k, '=', v)
