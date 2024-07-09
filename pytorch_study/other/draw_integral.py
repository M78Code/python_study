import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import matplotlib
import scipy.integrate as sci
from matplotlib.patches import Polygon


# 定义原函数
def _original_func(x):
    return x ** 2


# 计算积分
def _integral_func(x):
    result, _ = quad(_original_func, 0, x)
    return result


# 生成数据集
x = np.arange(0, 10, 0.1)
y = x ** 2

# 计算积分数据集
integral_y = np.vectorize(_integral_func)(x)


def _draw1():
    # 绘制原函数和积分函数图像
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Original Function: $x^2$')
    plt.plot(x, integral_y, label='Integral Function')
    # 填充积分区域
    plt.fill_between(x, 0, integral_y, alpha=0.6, color='gray')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Integral of $x^2$')
    plt.legend()
    plt.grid(True)
    plt.show()


_draw1()


def _integrand(x):
    return pow(x, 2)


# 计算定积分的值
a = 0
b = 2
integral_result, error = quad(_integrand, a, b)
# 创建等间距的x值数组
x_values = np.linspace(a, b, 1000)
# 计算对应的值（原函数）
y_values = pow(x_values, 2)
# 计算积分曲线上的y值（积分结果在整个区间上是一个常数）
integral_y_value = integral_result * np.ones_like(x_values)
# 绘制原函数曲线和积分线
plt.figure(figsize=(10, 8))
# 绘制x^2的图像
plt.plot(x_values, y_values, label='f(x)=x^2', color='blue')

# 绘制积分结果为一条直线
plt.plot([a, b], [integral_y_value[0], integral_y_value[-1]], label=f'∫f(x)dx from {a} to {b}', color='red',
         linestyle='--')

# 设置x轴刻度
plt.xticks([a, b], ['$a$', '$b$'])
# 添加网络，标题和标签
plt.grid(True)
plt.title('Integral of f(x) = x^2')

plt.xlabel('x')

plt.ylabel('y and ∫f(x)dx')

plt.legend()


# 显示图形
def d1():
    plt.show()


# d1()


def f(x):
    return np.sin(x) + 0.5 * x


a = 0.5
b = 9.5


# linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)    #np.linspace函数的参数,默认为分为50段
def _d2():
    x = np.linspace(0, 10)
    y = np.sin(x) + 0.5 * x
    fig, ax = plt.subplots(figsize=(7, 5))
    plt.plot(x, y, 'b', linewidth=2)
    plt.ylim(ymin=0)
    Ix = np.linspace(a, b)
    Iy = f(Ix)
    verts = [(a, 0)] + list(zip(Ix, Iy)) + [(b, 0)]
    poly = Polygon(verts, facecolor='0.7', edgecolor='0.5')  # 绘制曲线阴影部分
    ax.add_patch(poly)
    # matplotlib.axes._subplots.AxesSubplot
    #    labels
    plt.text(0.75 * (a + b), 1.5, r"$\int_a^b f(x)dx$", horizontalalignment='center', fontsize=20)
    plt.figtext(0.9, 0.075, '$x$')
    plt.figtext(0.075, 0.9, '$f(x)$')

    ax.set_xticks((a, b))
    ax.set_xticklabels(['$a$', '$b$'])
    ax.set_yticks([f(a), f(b)])
    plt.title('积分图')
    plt.show()


_d2()
