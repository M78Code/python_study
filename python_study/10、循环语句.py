# 循环语句
# 循环语句可以使指定的代码块重复指定的次数
# 循环语句分成两种，while循环 和 for循环
# while循环
# 语法:
#   while 条件表达式:
#       代码块
#   else:
#       代码块 （while循环结束后会执行此代码块）

# 循环的三个要素（表达式）
# 初始化表达式，通过初始化表达式初始化一个变量
i = 0

# 条件表达式，条件表达式用来设置循环执行的条件
while i < 10:
    print(f"Hello World {i}")
    # 更新表达式，修改初始化变量的值
    i += 1 # (冒似python中没有其他语言的 ++, -- 计算)


# break
# break可以用来立即循环语句（包括else）

# continue
# continue 可以用来跳过当次循环
# break和continue都是只对离他最近的循环起作用
    
# pass
# pass是用来在判断或循环语句中占位的

# 创建一个5次循环
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i+=1
else:
    print('循环结束')

j = 0
while j < 5:
    j += 1
    if j == 2:
        continue
    print(j)
else:
    print('循环结束')
