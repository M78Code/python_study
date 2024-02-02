# 布尔值（bool）
# 布尔值主要用来做逻辑判断
# 布尔值一共有两个True和False，都是大写
a = True
b = False

# 布尔值实际上也属于整型，True相当于1，False相当于0
print(a+1)
print(b+1)

# None（空值）
# None专门用来表示不存在
b = None
print(b)

# type()用来检查值的类型
# 该函数会将检查的结果作为返回值返回，可以通过变量来接收函数的返回值
c1 = type('123')
print(c1)       # <class 'str'>
c2 = type(a)    
print(c2)       # <class 'bool'>
c3 = type(b)
print(c3)       # <class 'NoneType'>    
