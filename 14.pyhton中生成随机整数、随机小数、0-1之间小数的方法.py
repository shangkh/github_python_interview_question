"""
随机整数：random.randint(a, b)，生成区间内的整数
随机小数：np.random.randn(5)，使用numpy库，生成5个随机小数
0-1随机小数：random.random()，括号中不传参数
"""

# 生成1个随机小数
import random

# 生成随机数，浮点类型
a = random.uniform(10, 20)
print(a)
# 控制随机数的精度round(数值，精度)
b = round(a, 2)
print(b)
