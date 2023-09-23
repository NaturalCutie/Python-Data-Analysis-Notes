# 18_列表
# 列表是一种数据结构，用于把相关联的数据整合在一起
# list = ["a", "b"]

# 1）针对列表的方法
# 方法与函数的区别：
# 对象.方法名(...);函数(参数)
# a.添加元素，只能通过方法添加一个元素
# 如：list.append("c")
# b.删除元素，只能通过方法删除一个元素
# 如：list.remove("a")

# 2）针对列表的python内置函数
# a.max(num_list)  返回列表里的最大值
# b.min(num_list)  返回列表里的最小值
# c.sorted(num_list)  返回由小到大排序好的新列表，同时不改变原先的列表

# 3）列表中可以放不同类型的数据
# a.列表可以通过len函数求长度
# b.列表可以通过索引
# I.返回某个位置的元素，如list[0]
# II.赋值，修改列表里的某个元素，如list[0] = "z"

# 4）列表等与其他数据类型的区别
# 列表等是可变的，字符串、整数、浮点数、布尔类型等不是
# 即其他数据类型只能被重新赋值；而列表可以通过append等方法，直接改变原列表。*列表也可以重新被赋值


# 例题1，运用1）和3）的知识
shopping_list = ['键盘', "音响"]
shopping_list.append('键帽')
shopping_list.remove('键帽')
shopping_list.append('音响')
shopping_list.append('电竞椅')

shopping_list[1] = '硬盘'  # 列表可以通过索引赋值，更改一个元素
print(shopping_list)
print(len(shopping_list))  # 返回列表中元素数量
print(shopping_list[2])  # 通过索引查找列表中第N个元素
print()

# 例题2，运用2）的知识
price = [799, 1024, 200, 800]
max_price = max(price)
min_price = min(price)
sorted_price = sorted(price)
print(max_price, min_price)
print(sorted_price)
price = [1, 2, 3]  # 列表也可以重新被赋值
