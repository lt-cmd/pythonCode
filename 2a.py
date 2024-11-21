import numpy as np

x = None
x0 = np.pi / 6
y0 = np.sin(x0)
x1 = np.pi / 4
y1 = np.sin(x1)
x2 = np.pi / 3
y2 = np.sin(x2)

def Lagrange_one(sign):
    if sign == 1:
        lag = ((x - x1) / (x0 - x1)) * y0 + ((x - x0) / (x1 - x0)) * y1
    elif sign == 2:
        lag = ((x - x2) / (x1 - x2)) * y1 + ((x - x1) / (x2 - x1)) * y2
    return lag


def Lagrange_two():
    lag = (((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))) * y0 + (
            ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))) * y1 + (
                  ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))) * y2
    return lag


def error(sign, a):
    if sign == 1:
        # 当flag = 1时，计算lagrange_one(1)所产生的误差。
        errorLeft = (-1 / 2) * (x - x0) * (x - x1) * y2
        errorRight = (-1 / 2) * (x - x0) * (x - x1) * y0
        errorResult = np.sin(x) - Lagrange_one(1)
        if errorResult > errorLeft and errorResult < errorRight:
            print(f"利用x0,x1推导出sin{a}°的值的误差在可接受范围内，且误差为:{errorResult}")
        else:
            print(f"利用x0,x1推导出sin{a}°的值的误差过大，请重新设计。（误差为：{errorResult}）")
    elif sign == 2:
        # 当flag = 2时，计算lagrange_one(2)所产生的误差。
        errorLeft = (-1 / 2) * (x - x1) * (x - x2) * y1
        errorRight = (-1 / 2) * (x - x1) * (x - x2) * y2
        errorResult = np.sin(x) - Lagrange_one(2)
        if errorResult > errorLeft and errorResult < errorRight:
            print(f"利用x0,x1推导出sin{a}°的值的误差在可接受范围内，且误差为:{errorResult}")
        else:
            print(f"利用x0,x1推导出sin{a}°的值的误差过大，请重新设计。（误差为：{errorResult}）")

    elif sign == 3:
        # 当flag = 3时，计算lagrange_two()所产生的误差。
        errorLeft = (-1 / 6) * (x - x0) * (x - x1) * (x - x2) * y0
        errorRight = (-1 / 6) * (x - x0) * (x - x1) * (x - x2) * y2
        errorResult = np.sin(x) - Lagrange_two()
        if errorResult > errorLeft and errorResult < errorRight:
            print(f"利用x0,x1推导出sin{a}°的值的误差在可接受范围内，且误差为:{errorResult}")
        else:
            print(f"利用x0,x1推导出sin{a}°的值的误差过大，请重新设计。（误差为：{errorResult}）")


a = input("请输入需要估算的sin函数的自变量x:")
x = float(a) * (np.pi / 180)

print(f'利用x0,x1可推导出sin{a}°的值为{Lagrange_one(1)}')
error(1, a)

print(f'利用x1,x2可推导出sin{a}°的值为{Lagrange_one(2)}')
error(2, a)

print(f'利用sinx的2次lagrange插值计算可推导出sin{a}°的值为{Lagrange_two()}')
error(3, a)
