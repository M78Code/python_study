import re

# 关于修饰符
result = re.search('a', 'ABC')
print(result)

# re.I, 忽略大小写
result = re.search('a', 'ABC', re.I).group()
print(result)

# re.M,
text = '第一行\n第二行\n第三行'
print(re.search('^.*$', text))
