# 一个print函数中只能包涵一种数据类型，print函数中可以用","将不同数据分隔开

# 6_
print('Dad')

# 7_1.字符串连接
# 把几个字符串可以通过"+"连接成一个更长的，再打印出来
# *引号包裹的字符串有空格，打印出来才有空格
print('D'+'a'+'d')

# 7_2.单双引号转义
# 单引号会和最近的单引号配对，双引号会和最近的双引号配对。
# 内容的引号是单，外面包裹字符串的引号得用双；内容的引号是双，外面包裹字符串的引号得是单；
# 或者用"\" + 单引号或者双引号，表明后面的引号是单纯的引号符号。
# （反斜杠是转义字符，表明后面的字符是纯字符，python会把反斜杠和后面的字符一起读）
print('"Hey,girl"')
print("I said \"Let\'s do sth!\"")
print("I said \"Let's do sth!\"")  # 包裹字符串的是双引号，内容的单引号也可以前面不用加转义字符

# 7_3.换行
# "\n" 表示换行
print('What\'s now? \nI don\'t know')

# 7_4.三引号跨行字符串
# 三个连续的单引号或者双引号，用它包裹住文字，python就会把新的一行当成内容的换行，而不是代码语句的结束。
print('''
春江潮水连海平，海上明月共潮生。
滟滟随波千万里，何处春江无月明！
江流宛转绕芳甸，月照花林皆似霰。
空里流霜不觉飞，汀上白沙看不见。
江天一色无纤尘，皎皎空中孤月轮。
江畔何人初见月？江月何年初照人？
人生代代无穷已，江月年年望相似。
不知江月待何人，但见长江送流水。
白云一片去悠悠，青枫浦上不胜愁。
谁家今夜扁舟子？何处相思明月楼？
可怜楼上月裴回，应照离人妆镜台。
玉户帘中卷不去，捣衣砧上拂还来。
此时相望不相闻，愿逐月华流照君。
鸿雁长飞光不度，鱼龙潜跃水成文。
昨夜闲潭梦落花，可怜春半不还家。
江水流春去欲尽，江潭落月复西斜。
斜月沉沉藏海雾，碣石潇湘无限路。
不知乘月几人归，落月摇情满江树。
''')
