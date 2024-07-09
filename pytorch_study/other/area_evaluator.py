import math


def f(x: float) -> float:
    return 4 / (math.pow(x, 2) + 1)


def _test_main():
    h = 0.0
    left_riemann = 0.0
    right_riemann = 0.0
    midpoint = 0.0
    a = 0.0
    b = 1.0
    h = b - a
    n = 1
    print("left Riemann Sum  Right Riemann Sum Midpoint Rule\n")
    while n <= 8192:
        n *= 2
        left_riemann = 0.0
        right_riemann = 0.0
        midpoint = 0.0
        i = 1
        while i <= n:
            i += 1
            # Left riemann sum.
            left_riemann += f(a + h * (i - 1.0))

            # Right riemann sum.
            right_riemann += f(a + h * (i))

            # Midpoint rule.
            midpoint += f(a + h * (i - 0.5))
        left_riemann *= h
        right_riemann *= h
        midpoint *= h
        print(f"{left_riemann} {right_riemann} {midpoint}\n")
        h /= 2.0


_test_main()
