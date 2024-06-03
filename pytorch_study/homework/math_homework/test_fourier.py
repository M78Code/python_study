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
    # np.linspace(-np.pi, np.pi, 60)
    for n in range(0, 61):
        x_m_n = x_m(n)
        x.append(x_m_n)

        y_m_n = f(x_m_n)
        y.append(y_m_n)

    # グラフのサイズ　面積=12cm * 10cm
    pt.figure(figsize=(12, 10))

    # グラフを描く
    pt.plot(x, y, label="f(x)関数の図")

    # 軸のラベルとタイトルの設定
    # mpl.rcParams["font.family"] = ["SimHei"]  # linux下設定的字体
    mpl.rcParams["font.family"] = ["Arial Unicode MS"]  # linux下设置的字体
    mpl.rcParams["axes.unicode_minus"] = False  # "UTF-8"
    pt.xlabel("x")
    pt.ylabel("f(x)")

    x_major_locator = MultipleLocator(1)
    ax = pt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    # 図例を示す
    pt.legend()

    # グラフを示す
    pt.show()


# _draw_sin()

def _draw_sin2():
    x = np.linspace(-np.pi, np.pi, 60)
    y = x * np.sin(x)

    size_ = np.sum(x * y)
    print(size_)

    # グラフのサイズ　面積=10cm * 8cm
    pt.figure(figsize=(12, 10))

    # グラフを描く
    pt.plot(x, y, label="f(x)2関数の図")

    # 軸のラベルとタイトルの設定
    # mpl.rcParams["font.family"] = ["SimHei"]  # linux下设置的字体
    mpl.rcParams["font.family"] = ["Arial Unicode MS"]  # linux下设置的字体
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


# _draw_sin2()

def f2(x):
    return 4 / (1 + pow(x, 2))


def _calcu_integral():
    left_riemann = 0.0
    right_riemann = 0.0
    midpoint_riemann = 0.0
    a = 0.0
    b = 1.0
    h = b - a
    for n in range(1, 100):
        for i in range(1, n):
            left_riemann += f2(a + h * (i - 1))
            right_riemann += f2(a + h * i)
            midpoint_riemann += f2(a + h * (i - 0.5))
        left_riemann *= h
        right_riemann *= h
        midpoint_riemann *= h
        print(f"left_riemann = {left_riemann}, right_riemann = {right_riemann},midpoint_riemann = {midpoint_riemann}")
        h /= 2.0


_calcu_integral()


def sectional_measurement():
    w = 1  # 長方形の幅
    x = np.arange(0, np.pi, w)  # x
    y = np.sin(x)  # y

    val = np.sum(y * w)  # 長方形の面積の合計
    print(val)


# if __name__ == '__main__':
#     sectional_measurement()


def _calcu_y_value_range():
    # x_array = []
    for n in range(1, 61):
        x_value_range = -3.14 + n / 10
        print(x_value_range)
        # x_array.append(x_value_range)
    # print(f"{len(x_array)}")
    # print(type(x_value_range))


# _calcu_y_value_range()
# _draw_sin2()
# _draw_sin()
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

fa = -np.pi * np.sin(-np.pi)
print(f"fa = {fa}")
