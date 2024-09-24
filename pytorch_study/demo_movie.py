import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

gendra_zero = pd.DataFrame()
gendra_zero.iloc()

import sympy as sp

y, n = sp.symbols('y n')

# 学习率
n = 0.2


# 更新梯度
def grad(x):
    return x - 2 * x * n


# 更新梯度方法
def grad_test():
    x_i = grad(10)
    for i in range(1000):
        if x_i <= 0.001:
            print(f'最终更新的梯度值结果{x_i}, i = {i}')
            break
        else:
            x_i = grad(x_i)
            print(format(x_i, '.5f'))
            # print(f'x_i: {x_i}')


grad_test()
