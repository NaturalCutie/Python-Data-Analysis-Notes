# 33_异常处理
# 一、异常类型
# 1.用长度之外的索引，对列表取值时，会产生IndexError,即索引错误
# number_list = [56, 23,-5, 96]
# number_list[4]
# 2.用数字除以0时，会产生ZeroDivisionError，即除零错误
# print(56 / (12 - 15 +3))
# 3.打开的文件不存在时，会产生FileNotFoundError,即找不到文件错误
# f = open("./hi.txt", "r")
# 4.让两个字符串做乘法，会产生TypeError,即类型错误
# "yoo" * "hi"
# ....

# 二、捕捉异常|try/except语句
# 1.try
# try语句换行后的代码块里，放上你觉得可能会产生报错的代码
# 2.except
# except后面，跟上你想捕捉的错误名字，以及冒号
# 换行后缩进的代码块里，放上那类错误发生后，你想相应执行的操作
# ！由于无法预判所有错误类型，如果你希望无论出现什么类型的错误，程序都不要炸的话
# 可以直接写个"except:"，这个语句会捕捉所有的错误类型
# *try/except语句，在捕捉错误时，从上往下运行。
# 如果第一个except语句就捕捉到了对应的错误，那后面的except语句都不会执行了
# 和if、elif的逻辑很像，只有第一个符合条件的分支会运行

# 3.else
# else语句换行后缩进的代码块里，放上当try里面的语句，没有产生任何错误时，要执行的语句
# 4.finally
# finally语句换行后缩进的代码块里，放上无论错误发生与否，最终都会被执行的语句
# *finally语句厉害的地方在于，无论是错误被某个except语句捕捉，还是没有任何错误产生，
# 还是出现了你没捕捉到的错误，把程序给炸了。finally里面的代码，最终都会被执行

# 以BMI指数程序为例，去捕捉异常
# user_weight = float(input("请输入您的体重(单位:kg):"))
# user_height = float(input("请输入您的身高(单位:m):"))
# user_BMI = user_weight / user_height ** 2
# print("您的BMI值为:" + str(user_BMI))

try:
    user_weight = float(input("请输入您的体重(单位:kg):"))
    user_height = float(input("请输入您的身高(单位:m):"))
    user_BMI = user_weight / user_height ** 2
except ValueError:
    print("输入不为合理数字，请重新运行程序，并输入正确的数字。")
except ZeroDivisionError:
    print("身高不能为零，请重新运行程序，并输入正确的数字。")
except:
    print("发生了未知错误，请重新运行程序。")
else:
    print("您的BMI值为:" + str(user_BMI))
finally:
    print("程序结束运行。")
