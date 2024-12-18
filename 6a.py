import numpy as np

# 高斯消元（列主元消去法）
def gaussian_elimination(A, b):
    n = len(b)

    for i in range(n):
        # 选取绝对值最大的元素作为主元素

        m=np.abs(A[i:, i])
        max_row = i + np.argmax(np.abs(A[i:, i]))
        # 交换最大值所在的行和第i行
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        print(A[i, i])
        # 检查主元是否为零
        # if A[i, i] == 0:
        #     raise ValueError("Matrix is singular and cannot be inverted.")

        # 消元
        for j in range(i + 1, n):
            # 计算因子
            factor = A[j, i] / A[i, i]
            # 将第j行减去factor乘以第i行
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]

    # 回代
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        # 检查主元是否为零
        # if A[i, i] == 0:
        #     raise ValueError("Matrix is singular and cannot be inverted.")
        # 处理边界条件，当i等于n-1时，没有后续元素可以点乘
        if i == n - 1:
            x[i] = b[i] / A[i, i]
        else:
            x[i] = (b[i] - np.dot(A[i, i + 1:n], x[i + 1:n])) / A[i, i]

    return x

A = np.array([[1.0, 1.0, 1.0], [0.0, 4.0, -1.0], [2.0, -2.0, 1.0]])
b = np.array([6.0, 5.0, 1.0])
try:
    result = gaussian_elimination(A, b)
    print("解为：x1 =", result[0], ", x2 =", result[1], ", x3 =", result[2])
except ValueError as e:
    print(e)