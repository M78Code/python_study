def f(x):
    return 4 / (1 + pow(x, 2))


def _calcu_pi_value():
    left_riemann = 0.0
    right_riemann = 0.0
    midpoint = 0.0
    a = 0.0
    b = 1.0
    h = b - a
    print("Left Riemann Sum   Right Riemann Sum   Midpoint Rule\n")
    n = 1
    while n <= 8192:
        n *= 2
        left_riemann = 0.0
        right_riemann = 0.0
        midpoint = 0.0
        for i in range(1, n):
            # Left riemann sum.
            left_riemann += f(a)
            pass
