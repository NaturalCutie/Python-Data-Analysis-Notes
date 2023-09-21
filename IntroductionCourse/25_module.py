# *在本文件中，模块指代标准库中的模块，模块、内置模块、标准库中的模块、标准库中的内置模块混用；
# *第三方库中的模块、第三方模块、第三方库混用。

# 内置函数、内置模块和第三方模块区别
# 1.内置函数、内置类型等，无需引入。
# 2.标准库中的内置模块，需要引入。
# 3.第三方模块，需要安装+引入。


# 一、调用内置函数
# python所有内置函数 https://docs.python.org/zh-cn/3/library/functions.html
print(sum([69, 124, -32, 27, 217]))


# 二、引入标准库中的模块
# 模块就是一个python程序。引入模块后，里面的函数和变量都可以为你所用。

# （一）、引入模块的方式
# 1.import语句
"""
import 模块名
模块名.函数名/模块名.变量名  来调用
"""
# 2. from...import...语句
"""
from 模块名 import 函数名/变量名  # 多个函数或变量用逗号进行分隔
函数名/变量名 直接使用
"""
# 3.from...import * 语句
"""
from 模块名 import *  # 会把模块里所有内容都进行引入
函数名/变量名 直接使用
* 不推荐使用，因为假如引入的模块A和B中都有abc函数，调用时不知是哪个模块的函数
"""

# （二）、标准库中的模块的使用
# python标准库里的所有模块 https://docs.python.org/zh-cn/3/library/index.html
# 点进模块就可以看到里面包含的函数和变量的用法和功能的介绍
# 在Pycharm，ctrl+左键点击函数名，查看定义函数的源代码

import statistics
print(statistics.median([69, 124, -32, 27, 217]))


# 三、第三方库的模块
# （一）、安装和引入第三方模块
# 1.安装
"""
进入终端
pip install 库名 
"""
# 2.引入
# 引入第三方库的模块的语法和前面一样

# （二）、第三方库中的模块的使用
# 搜索第三方库的网站 pypi.org
# 搜索后，点进模块可以查看介绍和用法

import akshare
print(akshare.get_cffex_daily("20220222"))  # 获取2022.2.22的中国金融期货交易所交易数据


# 另：statistics.median()源代码
def median1(data):
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise statistics.StatisticsError("no median for empty data")
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return (data[i - 1] + data[i]) / 2
# “%” 是取余的意思
# “//” 是向下取整的意思，如：3/2的结果为1.5，而3//2的结果为1
