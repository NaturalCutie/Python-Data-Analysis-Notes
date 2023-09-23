# 20_
# for 变量名 in 可迭代对象（list, dict, str, etc）
# 对列表进行迭代，就是按顺序对里面的各个元素操作；对字典进行迭代，就是按顺序对立面的各个键或值操作；对字符串进行迭代，就是按顺序对里面的各个字符操作。
# 自己取一个变量名来代表可迭代对象里面的东西，这个变量会被依次被赋值为如列表里的每一个元素。针对每个元素的操作，写在for的下面一行。
# 所有前面带缩进的都会被视为这个for循环里面的语句

# range()函数
# range用来表示整数序列。*range里第二个参数不在序列范围内
# 例1.range(100) 默认0是列表第一个元素，99为列表最后一个元素
# 例2.range(1, 100) 默认间隔1，列表里第一个元素为1，最后一个元素为99
# 例3.range(1, 100, 2) 列表里第一个元素为1，最后一个元素为99，间隔2

# 检查体温数字，找出不正常的低温
temperature_list = [36.4, 36.6, 37.5, 38.1, 39.3]
for temperature in temperature_list:
    if temperature >= 37.3:
        print(temperature)
        print("完球了")

# 利用字典，筛选出发烧的人
temperature_dict = {"111": 36.4, "112": 36.6, "113": 37.5, "114": 38.1, "115": 39.3}

for temperature_tuple in temperature_dict.items():
    staff_id = temperature_tuple[0]
    temperature = temperature_tuple[1]
    if temperature >= 37.3:
        print(staff_id)
# 字典名.items 在for循环时，变量会被赋值为键和值组成的元组。

# 另一种写法
# for staff_id, temperature in temperature_dict.items():
#     if temperature >= 37.3:
#         print(staff_id)
# 这里for循环后面跟了两个变量，这种写法相当于把元组的第一个元素赋值给第一个变量，第二个元素赋值给第二个变量。

# for循环结合range
total = 0
for i in range(1, 101):
    total = total + i
print(total)


