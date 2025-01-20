# 梯度下降法

import numpy as np


def f(x, y):
    return x ** 2 + y ** 2


# 定义目标函数的梯度
def gradient(x, y):
    # 对x求偏导
    grad_x = 2 * x
    # 对y求偏导
    grad_y = 2 * y
    return np.array([grad_x, grad_y])


def gradient_descent(gradient, start, learn_rate, n_iter=50, tolerance=1e-06):
    x, y = start
    for i in range(n_iter):
        grad = gradient(x, y)
        diff = -learn_rate * grad
        if np.linalg.norm(diff) < tolerance:
            print(f"在第 {i + 1} 次迭代时收敛。")
            break
        x = x + diff[0]
        y = y + diff[1]
        print(f"第 {i + 1} 次迭代：(x, y) = ({x:.6f}, {y:.6f})，f(x, y) = {f(x, y):.6f}")
    return x, y


# 设置初始值和学习率
start = np.array([10.0, 10.0])  # 初始值 (x, y)
learn_rate = 0.1  # 学习率

# 运行梯度下降算法
minimum = gradient_descent(gradient, start, learn_rate)
print(f"函数的最小值大约在 (x, y) = ({minimum[0]:.6f}, {minimum[1]:.6f})")
