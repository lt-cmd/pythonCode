import numpy as np

# 生成符合正态分布的随机数
def generate_normal_random_numbers(mean_values, standard_deviation, num_samples):
    return np.random.normal(mean_values, standard_deviation, num_samples)

# 隐藏层
def hidden_layer(x, hidden_w_list, hidden_b_list):
    hidden_list = np.dot(hidden_w_list, x) + hidden_b_list
    return hidden_list

# 输出层
def output_layer(hidden_list, output_w_list, output_b_list):
    output_list = np.dot(output_w_list, hidden_list) + output_b_list
    return output_list

# sigmoid激活函数
def sigmoid(input_array):
    return 1 / (1 + np.exp(-input_array))

# 误差
def error(output_list):
    c = np.array([0, 1])
    wucha = 0.5 * np.sum((c - output_list) ** 2)
    return wucha

mv = 0
sd = 1
num_samples = 36
x = np.array([1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1])

# 随机生成隐藏层的权重值（调用函数）
w_numbers = generate_normal_random_numbers(mv, sd, num_samples)
# 将随机数每 12 个一组放入元组，再将元组放入列表
hidden_w_list = w_numbers.reshape(3, 12)
# 输出隐藏层的权重值
print("隐藏层的权重值：", hidden_w_list)

# 随机生成隐藏层的偏置值（调用函数）
hidden_b_list = generate_normal_random_numbers(mv, sd, num_samples=3)
# 输出隐藏层的偏置值
print("隐藏层的偏置值：", hidden_b_list)

# 随机生成输出层的权重值（调用函数）
output_w_list = generate_normal_random_numbers(mv, sd, num_samples=6).reshape(2, 3)
# 输出输出层的权重值
print("输出层的权重值：", output_w_list)

# 随机生成输出层的偏置值（调用函数）
output_b_list = generate_normal_random_numbers(mv, sd, num_samples=2)
# 输出输出层的偏置值
print("输出层的偏置值：", output_b_list)

hidden_list = hidden_layer(x, hidden_w_list, hidden_b_list)
hidden_list = sigmoid(hidden_list)

output_list = output_layer(hidden_list, output_w_list, output_b_list)
output_list = sigmoid(output_list)

print("隐藏层输出：", hidden_list)
print("输出层输出：", output_list)
print("误差：", error(output_list))

# 分类判断
threshold = 0.5
if output_list[0] > threshold:
    print("该图像是数字0")
elif output_list[1] > threshold:
    print("该图像是数字1")
else:
    print("无法准确分类")