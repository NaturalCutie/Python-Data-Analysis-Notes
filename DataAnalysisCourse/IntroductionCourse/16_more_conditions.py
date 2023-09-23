"""
嵌套条件语句结构：
if [条件一]:
    if [条件二]:
        [语句A]
    else:
        [语句B]
else:
    [语句C]
"""

"""
多个条件判断结构：
if [条件一]:
    [语句A]
elif [条件二]:  # 如果条件二和条件三同时满足，python只会执行语句B。因为一旦执行那个分支，就不会再看同一层级下的其它条件判断了
    [语句B]
elif [条件三]:
    [语句C]
else:
    [语句D]
"""

# BMI = 体重 / 身高 ** 2
user_gender = input("请输入您的性别（男/女）：")
user_weight = float(input('请输入您的体重（单位：kg）：'))
user_height = float(input('请输入您的身高（单位：m）：'))
user_BMI = user_weight / user_height**2
print("您的BMI值为：" + str(user_BMI))

if user_gender == "男":
    if user_BMI <= 18.5:
        print("先生您好，此BMI属于偏瘦范围。")
    elif user_BMI <= 25:
        # 这里不用写成 "18.5 < BMI <= 25:"，因为BMI <= 18.5 的情况已经囊括在第一个分支里了
        print("先生您好，此BMI属于正常范围。")
    elif user_BMI <= 30:
        print("先生您好，此BMI属于偏胖范围。")
    else:
        print("先生您好，此BMI属于肥胖范围。")
else:
    if user_BMI <= 18.5:
        print("女士您好，此BMI属于偏瘦范围。")
    elif user_BMI <= 25:
        print("女士您好，此BMI属于正常范围。")
    elif user_BMI <= 30:
        print("女士您好，此BMI属于偏胖范围。")
    else:
        print("女士您好，此BMI属于肥胖范围。")
