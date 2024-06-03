def f(x):
    return 4 / (1 + pow(x, 2))


def _calcu_pi_value():
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


_calcu2_pi_value()
# result = format(1.23456, '0.3f')
#
# print(result)
#
# result = format(1.23456, '0.2f')
# print(result)
# result = format(1.23456, '0.4f')
# print(result)
# w = 1
# for k in range(0, w):
#     print(w)
