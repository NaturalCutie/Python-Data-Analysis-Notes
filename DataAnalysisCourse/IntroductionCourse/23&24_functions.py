# 23_定义函数
"""
def 函数名(参数1, 参数2):
    # 定义函数的代码
    # ...
# !定义函数的时候，里面的代码都不会被执行；只有在调用函数的时候，才是里面的代码被实际执行的时候
"""


# 定义一个计算扇形面积的函数
def calculate_sector(central_angle, radius):
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print(f"此扇形面积为：{sector_area}")


calculate_sector(180, 1)  # 调用函数时，central_angle和radius两个参数会被赋值为传入的值


# 24_
# 1.作用域
# 在函数里定义的变量是局部变量，在函数内部可以访问到，在外部无法访问到。
# *通过调用函数来运行某段代码，和直接运行某段代码，并不是完全一样的。
# 2.return语句
# return a, b, c
# ！return后跟上两个及以上变量的时候，返回这些变量的值组成的元组
# 1)有return语句，函数在执行时，不仅会逐行运行里面的语句，还会在完成调用后，返回变量的值
# 2)在没写return语句时，python函数的返回值会默认为None。
# !print, append等实质上都是返回值为None的函数；len, sum等都是带返回值的函数，所以一般会把这些函数的调用结果赋值给其他变量。
# 如：result = print("Hi!")，result值为None； result = len("Hi!")，result值为3

# 写一个BMI计算器函数，可以计算出任意体重和身高的BMI值，并返回出计算的BMI值
def calculate_BMI(weight, height):
    BMI = weight / height ** 2
    if BMI <= 18.5:
        category = '偏瘦'
    elif BMI <= 25:
        category = '正常'
    elif BMI <= 30:
        category = '偏胖'
    else:
        category = '肥胖'
    print(f"您的BMI分类为：{category}")
    return BMI


weight = float(input('请输入您的体重（单位：kg）：'))
height = float(input('请输入您的身高（单位：m）：'))
BMI = calculate_BMI(weight, height)  # 执行函数，同时将返回值赋值给BMI
# calculate_BMI(weight,height)  # 只执行函数
print(f'您的BMI为{BMI:.2f}')
