import numpy as np


def _test_sectional_measurement():
    w = 0.1  # 長方形の幅
    x = np.arange(0, np.pi, w)
    y = np.sin(x)
    val = np.sum(y * w)
    print(val)
    # for e in x:
    #     y = np.sin(e)  # y
    #     val = np.sum(y * w)  # 長方形の面積の合計
    #     print(val)


# _test_sectional_measurement()

print(np.arange(0, np.pi, 0.1))
