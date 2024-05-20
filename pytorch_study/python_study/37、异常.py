# 处理异常
# 程序运行时出现异常，可以进行异常处理
# try语句 可以将可能出错的代码放入到try语句，
# 如果出现错误，则会执行except子句中的代码，
print("try异常学习")
try:
    # try中放置的是有可能出现错误的代码
    a = 10 / 0
except ZeroDivisionError as e:
    # except中放置的是出错后的处理
    print("程序出错了")
else:  # 可写可不写
    print(a)
finally:  # 无论是否有异常都要执行
    pass
