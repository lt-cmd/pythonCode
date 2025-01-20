from sympy import *
import numpy as np

x = symbols('x')

xishu = ([[1, 1, 1, 1], [0, 1, 2, 3], [0, 1, 4, 9], [0, 1, 8, 27], [0, 1, 16, 81]])

l0 = ((x - 1) * (x - 2) * (x - 3)) / ((-1) * (-2) * (-3))
l1 = ((x - 0) * (x - 2) * (x - 3)) / ((1) * (-1) * (-2))
l2 = ((x - 0) * (x - 1) * (x - 3)) / ((2) * (1) * (-1))
l3 = ((x - 0) * (x - 1) * (x - 2)) / ((3) * (2) * (1))

A = [None, None, None, None]

f = [1, x, x ** 2, x ** 3, x ** 4]


def coefficient(l0, l1, l2, l3):
    A[0] = integrate(l0, (x, 0, 3))
    A[1] = integrate(l1, (x, 0, 3))
    A[2] = integrate(l2, (x, 0, 3))
    A[3] = integrate(l3, (x, 0, 3))


def Verification(A, f):
    for i in range(5):
        F = integrate(f[i], (x, 0, 3))
        s = A[0] * xishu[i][0] + A[1] * xishu[i][1] + A[2] * xishu[i][2] + A[3] * xishu[i][3]
        if F == s:
            print(f"f(x)={f[i]}时精确成立")
        else:
            print(f"f(x)={f[i]}时不精确成立，所以该求积公式的代数精度为{i - 1}")
            print(f"本题中的积分约等于{A[0]}*f(0)+{A[1]}*f(1)+{A[2]}*f(2)+{A[3]}*f(3)")


coefficient(l0, l1, l2, l3)
Verification(A, f)
