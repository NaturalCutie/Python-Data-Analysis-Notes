# 21_
"""
while 条件A:
    行动B
# 计算机会判断条件A是否为真，如果为真，执行行动B；然后再次判断条件是否为真，再次执行行动B；如此循环，直到条件为假，退出循环
# *如果while后面的条件A，在第一次判断的时候就为False，那么行动B一次也不会被执行
"""
# for循环与while循环
# for循环一般有明确循环对象或次数；while循环一般循环次数未知

# 一个对用户输入数字求平均值的计算器，这个计算器的特点是用户可以输入任意数量的数字
print("你好，我可以帮你求平均值！")
num = input("请输入数字(完成所有输入后，请输入q终止程序）：")
total = 0
i = 0
while num != 'q':
    total += float(num)     # total += float(num) 相当于 total = total + float(num)
    i += 1
    num = input("请输入数字(完成所有输入后，请输入q终止程序）：")
if total == 0:
    result = 0
else:
    result = total / i
# 预防用户第一次就输入q，使得result = 0 / 0,导致报错
print("平均值为：" + str(result))
