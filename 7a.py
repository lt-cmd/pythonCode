import numpy as np

# 定义方程函数
def f(x):
    return x ** 3 - x - 1

# 二分法求解函数
def bisection_method(a, b, error):
    mid_prev = None  # 先初始化为None，表示还未开始正常比较差值
    while True:
        mid = (a + b) / 2  # 计算当前区间中点（新的近似根）
        if mid_prev is not None and abs(mid - mid_prev) <= error:  # 从第二次迭代开始判断差值是否满足精度要求
            return round(mid, 2)  # 满足则返回，保留两位小数
        mid_prev = mid  # 更新上一次的近似根为当前的近似根
        if f(mid) == 0:
            return round(mid, 2)
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid

a = 1.0
b = 1.5
error = 0.01
root = bisection_method(a, b, error)
print("近似根为:", round(root, 2))