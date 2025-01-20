from sympy import *
import numpy as np

x = Symbol('x')
y = exp(x)

# 计算基函数和原函数的内积
inner_product = [None, None, None, None]
inner_product[0] = integrate(y, (x, -1, 1))
inner_product[0] = round(inner_product[0], 4)
inner_product[1] = integrate(y * x, (x, -1, 1))
inner_product[1] = round(inner_product[1], 4)
basis_function2 = ((3 * (x ** 2) - 1) / 2) * y
inner_product[2] = integrate(basis_function2, (x, -1, 1))
inner_product[2] = round(inner_product[2], 5)
basis_function3 = ((5 * (x ** 3) - 3 * x) / 2) * y
inner_product[3] = integrate(basis_function3, (x, -1, 1))
inner_product[3] = round(inner_product[3], 5)

for i in range(4):
    print(inner_product[i])

# 计算多项式系数
aK = [None, None, None, None]
for i in range(4):
    aK[i] = inner_product[i] * ((2 * i + 1) / 2)
    aK[i] = round(aK[i], 4)

for i in range(4):
    print(aK[i])

# 三次最佳平方逼近多项式
s = aK[0] * 1 + aK[1] * x + aK[2] * ((3 * (x ** 2) - 1) / 2) + aK[3] * (((5 * ((x) ** 3)) - 3*x) / 2)

# 误差计算
errorList = [None, None, None, None]
errorTotel = 0.000000
for i in range(4):
    errorList[i] = (2 / (2 * i + 1)) * (aK[i]) ** 2
    errorTotel += errorList[i]
    errorTotel = round(errorTotel, 6)

error1 = integrate(y ** 2, (x, -1, 1))
error1 = round(error1, 6)
error = round(error1 - errorTotel, 6)
print(error)
