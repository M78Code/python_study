import math

import numpy as np
from matplotlib.patches import Polygon
from matplotlib.pyplot import MultipleLocator
from pylab import mpl
import matplotlib.pyplot as pt
import matplotlib
from scipy.integrate import quad


# y関数の定義
def func(x):
    return x * np.sin(2 * x)


# xの値の範囲、60部分を分割する
x = np.linspace(-np.pi, np.pi, 60)
# y関数
y = func(x)


def integral_func(x):
    result, _ = quad(func, -np.pi, np.pi)
    return result


# 積分を計算する
integral_y = np.vectorize(integral_func)(x)


# 図を描く
def _draw_figure():
    pt.figure(figsize=(12, 10))

    # グラフを描く
    pt.plot(x, y, label="f(x)関数の図")
    pt.plot(x, integral_y, label='積分の図', color='red')
    # 填充积分区域
    pt.fill_between(x, y, where=(y < 0), interpolate=True, alpha=0.2, color='gray')
    pt.fill_between(x, y, where=(y > 0), interpolate=True, alpha=0.2, color='green')

    # print(f"{format(, '0.15f')})
    # print("integral_y", integral_y)

    # 軸のラベルとタイトルの設定
    # mpl.rcParams["font.family"] = ["SimHei"]  # linux下設定的字体
    mpl.rcParams["font.family"] = ["Arial Unicode MS"]  # linux下设置的字体
    mpl.rcParams["axes.unicode_minus"] = False  # "UTF-8"
    # pt.xlabel("x")
    pt.ylabel("f(x)")

    x_major_locator = MultipleLocator(1)
    ax = pt.gca()
    # 図名
    ax.set_title('y = x * sin(2x)')

    # 右の枠線を表示しない
    ax.spines['right'].set_visible(False)
    # 上の枠線を表示しない
    ax.spines['top'].set_visible(False)
    # デフォルト軸位置の変更
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    ax.xaxis.set_major_locator(x_major_locator)

    # 図例を示す
    pt.legend()

    # グラフを示す
    pt.show()


_draw_figure()


def f(x):
    return x * np.sin(x)


def _calcu_pi_value():
    left_riemann = -np.pi
    right_riemann = np.pi
    midpoint = 0.0
    a = 0.0
    b = 1.0
    h = b - a
    print("Left Riemann Sum    Right Riemann Sum   Midpoint Rule\n")
    n = 1
    while n <= 8192:
        left_riemann = 0.0
        right_riemann = 0.0
        midpoint = 0.0
        for i in range(0, n):
            # Left riemann sum.
            left_riemann += f(a + h * (i - 1.0))
            # Right riemann sum.
            right_riemann += f(a + h * i)
            # Midpoint rule.
            midpoint += f(a + h * (i - 0.5))

        left_riemann *= h
        right_riemann *= h
        midpoint *= h
        print(f"{format(left_riemann, '0.15f')}   {format(right_riemann, '0.15f')}   {format(midpoint, '0.15f')}")
        h /= 2.0
        n *= 2


# _calcu_pi_value()

def _calcu2_pi_value():
    left_riemann = 0.0
    right_riemann = 0.0
    midpoint = 0.0
    a = 0.0
    b = 1.0
    h = b - a
    print("Left Riemann Sum    Right Riemann Sum   Midpoint Rule\n")
    n = 1
    while n <= 8192:
        left_riemann = 0.0
        right_riemann = 0.0
        midpoint = 0.0
        i = 1
        while i <= n:
            # Left riemann sum.
            left_riemann += f(a + h * (i - 1.0))
            # Right riemann sum.
            right_riemann += f(a + h * i)
            # Midpoint rule.
            midpoint += f(a + h * (i - 0.5))

            i += 1

        left_riemann *= h
        right_riemann *= h
        midpoint *= h
        print(f"{format(left_riemann, '0.15f')}   {format(right_riemann, '0.15f')}   {format(midpoint, '0.15f')}")
        h /= 2.0
        n *= 2

# _calcu2_pi_value()
