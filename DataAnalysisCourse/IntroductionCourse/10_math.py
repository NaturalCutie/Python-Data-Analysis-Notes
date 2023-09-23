# 通过官方文档了解标准库里包含哪些函数
import math  # 引入标准库中的math模块

a = 1
b = 9
c = 20
delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)  # 使用模块里的函数或变量时，用 模块名.函数名/模块名.变量名 来使用。
x2 = (-b - math.sqrt(delta)) / (2 * a)  # (其实这里也可以写作delta ** (1/2))
print(x1)
print(x2)
