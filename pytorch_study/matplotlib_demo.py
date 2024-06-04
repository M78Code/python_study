# 1. 基本包的导入
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 程序目的 在特定位置添加坐标轴

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 制图
def draw1():
    # 2.1 制图数据
    x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
    y = np.sin(x)
    # 2.2 创建制图对象
    # fig, ax = plt.figure(figsize=(8, 6), dpi=600)
    fig, ax = plt.subplots()
    # 2.3 绘图
    ax.plot(x, y)
    ax.set_title('y = sin(x)')  # 图名
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # 2.4 特定位置建立坐标轴
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    # axes_1的x轴字体设置
    # x1_label = ax.get_xticklabels()
    # [x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
    # y1_label = ax.get_xticklabels()
    # [y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]
    # 2.5 坐标轴刻度间隔设置
    ax.set_yticks(np.arange(-1, 1.1, 0.5))
    ax.set_xticks(np.arange(-2 * np.pi, 2 * np.pi + 0.1, 0.5 * np.pi))
    # 2.6 坐标轴标签设置
    # labels = [str(ii) + '$\pi$' for ii in [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]]

    # 2.7 新建axes子图形ax_2，在特定位置添加坐标轴
    # ax_2 = ax.twinx()
    # [ax_2.spines[ii].set_visible(False) for ii in ['left', 'bottom']]
    # # 在子图形ax_2的y=0.8处新建坐标轴
    # ax_2.spines['top'].set_position(('data', 0.8))
    # ax_2.spines['top'].set_color('r')
    # # 在子图形ax_2的x=2.5*np.pi处新建y轴
    # ax_2.spines['right'].set_position(('data', 2.5 * np.pi))
    # ax_2.spines['right'].set_color('r')
    # ax_2.tick_params(axis='y', labelsize=9,  # y轴字体大小设置
    #                  color='r',  # y轴标签颜色设置
    #                  labelcolor='r',  # y轴字体颜色设置
    #                  direction='out'  # y轴标签方向设置
    #                  )
    # ax_2.set_ylabel('新建y轴', color='r')
    plt.show()


# draw1()

# original function
def original_func(x):
    return pow(x, 2)


def integral_func(x):
    result, _ = quad(original_func, 0, x)
    return result


# 生成数据集
x = np.arange(0, 10, 0.1)
y = x ** 2

# 计算积分数据集
integral_y = np.vectorize(integral_func)(x)


def draw2():
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Original Function: $x^2$')
    plt.plot(x, integral_y, label='Integral Function')
    plt.fill_between(x, 0, integral_y, color='gray')  # 填充积分区域
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Integral of $x^2$')
    plt.legend()
    plt.grid(True)
    plt.show()


draw2()
