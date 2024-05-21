import numpy as np
from matplotlib.pyplot import MultipleLocator
from pylab import mpl
import matplotlib.pyplot as pt


# フーリエ級数
# 問題5、フーリエ級数を求めて、グラフを描け

# 関数の定義
def f(x):
    return x * np.sin(x)


def x_m(n):
    return -np.pi + 0.1 * n


def _draw_sin():
    # x軸の値の配列
    x = []

    # x値について計算したy軸の値配列
    y = []

    # ループ計算するxとyの値
    for n in range(0, 61):
        x_m_n = x_m(n)
        x.append(x_m_n)

        y_m_n = f(x_m_n)
        y.append(y_m_n)

    # グラフのサイズ　面積=10cm * 8cm
    pt.figure(figsize=(10, 8))

    # グラフを描く
    pt.plot(x, y, label="f(x)関数の図")

    # 軸のラベルとタイトルの設定
    mpl.rcParams["font.family"] = ["SimHei"]
    mpl.rcParams["axes.unicode_minus"] = False
    pt.xlabel("x")
    pt.ylabel("f(x)")

    x_major_locator = MultipleLocator(1)
    ax = pt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    # 図例を示す
    pt.legend()

    # グラフを示す
    pt.show()


_draw_sin()

# xの範囲 -PI <=x<= PI x(-PIからPIまで)
# x = np.linspace(-np.pi, np.pi)

# nの範囲は配列[1, 60]の間にの整数
# n = range(1, 61)  # 1 <= n < 61


# グラフのサイズ　面積=10cm * 8cm
# pt.figure(figsize=(10, 8))

#
# pt.plot(x, f(x), label="sin(x)", color='red')
# pt.plot(x, f(x), label="cos(x)", color='blue')

# 軸のラベルとタイトルの設定
# mpl.rcParams["font.family"] = ["Ubuntu Sans"]
# mpl.rcParams["axes.unicode_minus"] = False
# pt.xlabel('x')
# pt.ylabel('f(x)')
# pt.title('周期関数f(x)のフーリエ級数のグラフ')

# pt.legend()

# グラフを示す
# pt.show()
