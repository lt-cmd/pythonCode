import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

# 全局设置中文字体
rcParams['font.family'] = 'SimHei'  # 'SimHei' 是黑体的字体名
rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 函数形式
def f(x, y):
    return y - (2 * x) / y


# 显式欧拉
def Explicit_Euler(x0, y0, h, x_end):
    x = []
    y = []
    x.append(x0)
    y.append(y0)

    while x[-1] < x_end:
        x_next = x[-1] + h
        y_next = y[-1] + h * f(x[-1], y[-1])
        x.append(x_next)
        y.append(y_next)

    return x, y


# 隐式欧拉
def Implicit_Euler(x0, y0, h, x_end):
    x = []
    y = []
    x.append(x0)
    y.append(y0)

    while x[-1] < x_end:
        x_next = x[-1] + h
        y_next = y[-1] + h * f(x[-1], y[-1])
        for _ in range(10):
            y_next_new = y[-1] + h * f(x_next, y_next)
            residual = y_next_new - y_next
            if abs(residual) < 1e-6:
                break
            y_next = y_next_new  # 更新 y_next
        x.append(x_next)
        y.append(y_next)

    return x, y


# 两步欧拉(预测—校正)
def Two_step_Euler(x0, y0, h, x_end):
    x = []
    y = []
    x.append(x0)
    y.append(y0)

    while x[-1] < x_end:
        x_next = x[-1] + h
        # 预测
        y_predict = y[-1] + h * f(x[-1], y[-1])
        # 校正
        y_next = y[-1] + (h / 2) * (f(x[-1], y[-1]) + f(x_next, y_predict))
        x.append(x_next)
        y.append(y_next)

    return x, y


# 初始参数
x0 = 0
y0 = 1
x_end = 1
# 步长
h = 0.1
true_x = np.arange(x0, x_end + h, h)
true_y = [1.0000, 1.0954, 1.1832, 1.2649, 1.3416, 1.4142, 1.4832, 1.5492, 1.6125, 1.6733, 1.7321]

# 执行显式欧拉方法
x, y = Explicit_Euler(x0, y0, h, x_end)
# 执行隐式欧拉方法
m, n = Implicit_Euler(x0, y0, h, x_end)
# 执行两步欧拉(预测—校正)方法
a, b = Two_step_Euler(x0, y0, h, x_end)

# 打印结果
print("显式欧拉结果为：")
for i in range(len(x) - 1):
    print(f"x = {x[i]:.2f}, y = {y[i]:.4f}")
print("====================================")
print("隐式欧拉结果为：")
for i in range(len(m) - 1):
    print(f"x = {m[i]:.2f}, y = {n[i]:.4f}")
print("====================================")
print("两步欧拉(预测—校正)结果为：")
for i in range(len(m) - 1):
    print(f"x = {a[i]:.2f}, y = {b[i]:.4f}")

plt.figure(figsize=(10, 6))
plt.plot(true_x, true_y, 'k-', label='真实解')  # 真实解
plt.plot(x, y, 'b-o', label='显式欧拉')  # 显式欧拉
plt.plot(m, n, 'r-s', label='隐式欧拉')  # 隐式欧拉
plt.plot(a, b, 'g-^', label='两步欧拉(预测—校正)')  # 两步欧拉
plt.xlabel('x')
plt.ylabel('y')
plt.title('欧拉方法的比较')
plt.legend()
plt.grid(True)
plt.show()