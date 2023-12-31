# 36_高阶函数和匿名函数
# 定义一个函数，能打印某数字平方和三次方的结果，还能打印某数字加10后的结果
# 假如把计算和打印的过程逻辑都保留在这个函数里，则无法优雅直观地定义函数
# 把计算平方、三次方、加10的函数独立出来，再把做计算的函数直接作为参数传入，逻辑更清晰直观
def calculate_square(num):
    return num * num


def calculate_cube(num):
    return num * num * num


def calculate_plus_10(num):
    return num + 10


def calculate_and_print(num, calculate):
    result = calculate(num)
    print(f"""
|数字参数|{num}|
|计算结果|{result}|""")


calculate_and_print(3, calculate_square)
calculate_and_print(7, calculate_plus_10)


# 一、高阶函数
# 1.定义：把函数作为参数的函数叫做高阶函数
# *作为参数的函数，是直接用函数名进行传入，代表函数本身，后面不要带括号和参数
# *用函数名作为参数，代表函数本身；而用函数名带上括号作为参数，这个函数就被调用了，传入的是函数调用后返回的结果
# 2.用处：高阶函数给程序提供了更多灵活性：高阶函数负责核心功能，作为参数的函数负责实现多样化的功能

# 二、匿名函数 lambda表达式被用于创建匿名函数
# 1.应用场景
# 适合函数作为高阶函数的参数，只需要一次性调用的场景
# 2.由于匿名函数的定义，是由lambda这个关键字开始的，所以可以用lambda指代匿名函数
# 3.用法
# 在高阶函数的括号里，放上关键字lambda，跟上变量名，然后是冒号，然后是返回的结果
# 冒号前面的变量名，表示的是传给匿名函数的参数
# 如果要给匿名函数增加参数，只需要在lambda关键字后面，把参数用不同逗号分隔开
calculate_and_print(7, lambda num: num * 5)
# 4.特点
# 匿名函数能减少代码行数，不用起名字，不用换行缩进，特别适合只需要一次性调用的场景
# 匿名函数：
# lambda num1, num2: num1 + num2
# 普通函数：
# def calculate_sum(num1, num2):
# return num1 + num2
# 5.匿名函数除了作为高阶函数的参数，也可以定义好后被直接调用
# 调用方式和普通函数类似，都是函数后面括号，括号里传入参数。唯一的区别是，前面的匿名函数也要被括住，表示这是一个整体
(lambda num1, num2: num1 + num2)(2, 3)
# 6.局限性
# 普通函数可以有多个语句/表达式，而匿名函数冒号后面只能有一个语句/表达式，
# 只适用于简单的场景，多步骤的复杂逻辑，或者是涉及循环递归等无法用匿名函数写出来
# 或者即使有些逻辑能用匿名函数写出来，可读性也会很差
