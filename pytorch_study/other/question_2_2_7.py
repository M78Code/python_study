#
# 関数f(x)は次のように与えられていて、f(x)は周期2PIを持つとする。f(x)のフーリエ級数を求めて、
# 最初の３つの部分和の正確なグラフを描け。
# f(x) = x(-PI < X < PI)
#

import numpy as np
import matplotlib.pyplot as pt

# 周期関数 f(x) = x
x_ = np.linspace(-np.pi, np.pi, 60)
print(x_)


def f(x):
    return x


def fourier_func(x):
    return -2 * (np.sin(x))


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


for i in range(1, 1000):
    sum_ = 0
    count = 0
    check_count = 0
    j_array = []
    for j in range(1, i):

        if i % j == 0:
            count += 1
            check_count += 1
            sum_ += j
            j_array.append(j)
            if sum_ == i:
                print(f"j = {j},i={i}, j_array={j_array}")
                j_array.clear()
            else:
                check_count += 1
        else:
            pass
    # if x % 2 == 0:

# for ii in range(5):
#     for jj in range(ii):
#         print(f"ii = {ii}, jj={jj}")

# from matplotlib.font_manager import FontManager
#
# fm = FontManager()
# mat_fonts = set(f.name for f in fm.ttflist)
# print(mat_fonts)
