#
# 関数f(x)は次のように与えられていて、f(x)は周期2PIを持つとする。f(x)のフーリエ級数を求めて、
# 最初の３つの部分和の正確なグラフを描け。
# f(x) = x(-PI < X < PI)
#

import numpy as np
import matplotlib.pyplot as pt

# 周期関数 f(x) = x
x_ = np.linspace(-np.pi, np.pi)


def f(x):
    return x


def fourier_func(x):
    return -2(np.sin(x))

# x = np.arange(0, 360)
# # 如果打印x, NumPy 会给你很好看的打印格式
# # print(x)
# y = np.sin(x * np.pi / 180)
# pt.plot(x, y)
# pt.xlim(0, 360)
# pt.ylim(-1.2, 1.2)
#
# pt.title('Sine wave')
#
# pt.show()
