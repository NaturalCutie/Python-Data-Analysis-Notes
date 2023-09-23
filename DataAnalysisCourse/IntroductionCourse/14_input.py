# input函数
# input()，里面放字符串，作为给用户的提示信息；
# 需要用一个变量去获取input函数返回的值。

# *input函数返回的值为str类型，
# 特别是用户输入的是数字，且后续需要做条件判断的时候：需要将输入信息转换成int类型或float类型，才能做条件判断

# int函数、float函数、str函数
# 以int函数举例，可以将str类型或float类型转换成int类型，*函数里的参数必须确实能被转化为整数
# str函数在print时很有用，将int类型或float类型转化成字符串后，和其他字符串一起打印

# BMI = 体重 / 身高 ** 2
user_weight = float(input('请输入您的体重（单位：kg）：'))
user_height = float(input('请输入您的身高（单位：m）：'))
user_BMI = user_weight / user_height ** 2
print("您的BMI值为：" + str(user_BMI))
