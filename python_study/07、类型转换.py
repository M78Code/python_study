# 类型转换
#  所谓的类型转换，将一个类型的对象转换为其他对象
# 类型转换四个函数int() float() str() bool()
# int()可以用来将其他的对象转换为整型

# 规则
# 布尔值: True -> 1   False -> 0
# 浮点数: 直接取整，省略小数点后的内容
# 字符串: 合法的整数字符串，直接转换为对应的数字，不合法报错ValueError: invalid ...
# float() 和 int()基本一致，不同的是它会将对象转换为浮点数
# str()可以将对象转换为字符串

# bool()可以将对象转换为布尔值，任何对象都可以转换为布尔值
# 规则:对于所有表示空性的对象都会转换为False，其余的转换为True
#       哪些表示的空性: 0, None, '' ...

a = True
print(f"初始值a = {a}")
# 调用int()函数来将a转换为整型
a = int(a)
print(f"调用int函数后的a = {a}")

x = "a"
print(f"id值 = {id(x)}")
x = x.encode
print(f"x的值为 {x}")
