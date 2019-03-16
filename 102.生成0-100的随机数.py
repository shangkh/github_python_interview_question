import random

res1 = 100 * random.random()  # random.random()生成的是0-1之间的随机小数，所以乘100
res2 = random.choice(range(0, 101))
res3 = random.randint(1, 100)

print(res1)
print(res2)
print(res3)
