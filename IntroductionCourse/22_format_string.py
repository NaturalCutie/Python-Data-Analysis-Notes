# 22_格式化字符串
# 花括号表示会被替换的位置

# 一、format方法
# 1.根据参数位置替换
# 花括号里面用数字表示参数位置，表示会用format里面的第几个参数进行替换 *0表示第一个参数
# 2.根据关键词替换
# 花括号里面用关键词来指定替换的对象。 *此时format里面参数位置就无所谓了

# 二、f-字符串
# 在字符串前加前缀“f”，花括号里面放入变量，花括号里的内容会被直接求值，添加到字符串内
# f-字符串方法，花括号内可以放入算式，进行计算求值后添加到字符串内

# !用format方法或f-字符串自动将，花括号中其他数据类型转化成str

# 根据参数位置
year = "虎"
name = '老郑'
message_content1 = """
律回春渐，新元肇启。
新岁甫至，福气东来。
金{0}贺岁，欢乐祥瑞。
金{0}敲门，五福临门。
给{1}及家人拜年啦！
新春快乐，{0}年大吉!
""".format(year, name)
print(message_content1)

# 根据关键词
message_content2 = """
律回春渐，新元肇启。
新岁甫至，福气东来。
金{current_year}贺岁，欢乐祥瑞。
金{current_year}敲门，五福临门。
给{receiver_name}及家人拜年啦！
新春快乐，{current_year}年大吉!
""".format(current_year=year,
           receiver_name=name)  # format函数中current_year是关键词；year是format函数的参数，也是变量
# """.format(year=year, name=name)  # 也可以如此表示，等号前面是关键词，等号后面是参数
print(message_content2)

# f-字符串
message_content = f"""
律回春渐，新元肇启。
新岁甫至，福气东来。
金{year}贺岁，欢乐祥瑞。
金{year}敲门，五福临门。
给{name}及家人拜年啦！
新春快乐，{year}年大吉!
"""

# 对数字格式化
gpa_dict = {'小明': 3.251, '小花': 3.869, '小李': 2.683, '小张': 3.685}
for name, gpa in gpa_dict.items():
    print("{0}你好，你的当前绩点为：{1:.2f}".format(name, gpa))
    # print(f"{name}你好，你的当前绩点为：{gpa:.2f}")  # “:.Nf” 来指定浮点数在格式化时保留几位小数
