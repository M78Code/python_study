import numpy as np
from pylab import mpl
import matplotlib.pyplot as pt

# フーリエ級数
# 問題5、フーリエ級数を求めて、グラフを描け

n = range(0, 61)  # 0 <= n < 61

# xの範囲 -PI <=x<= PI x(-PIからPIまで)
x = np.linspace(-np.pi, np.pi)


# 関数の定義
def f(_x):
    return _x * np.sin(2 * _x)


# グラフのサイズ　面積=10cm * 8cm
pt.figure(figsize=(10, 8))

# グラフを描く
pt.plot(x, f(x), label="sin(x)", color='red')
# pt.plot(x, f(x), label="cos(x)", color='blue')

# 軸のラベルとタイトルの設定
# mpl.rcParams["font.family"] = ["Ubuntu Sans"]
mpl.rcParams["axes.unicode_minus"] = False
pt.xlabel('x')
pt.ylabel('f(x)')
pt.title('周期関数f(x)のフーリエ級数のグラフ')

# 図例を示す
pt.legend()

# グラフを示す
pt.show()


