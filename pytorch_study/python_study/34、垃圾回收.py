# 在程序中没有被引用的对象就是垃圾，所谓的垃圾回收就是讲垃圾对象从内在中删除
# Python中有自动的垃圾回收机制，它会自动将这些没有被引用的对象删除
#   不用手动处理垃圾回收
class A:
    def __init__(self):
        self.name = "Python"

    # del 是一个特殊方法，它会在对象被垃圾回收前调用
    def __del__(self):
        print("A()对象被删除了～～～", self)


a = A()
print(a.name)

# a = None  # 将a设置为了None，此时没有任何的变量对A()对象进行引用，就变成了垃圾
# input('回车键退出...') #加上input后，等程序运行结束
