# 元组tuple
# example_tuple = ("张伟", "33")
# 1）是python中一种不可变的数据类型。*由于元组不可变，添加、删除元素等统统不能操作。
# 2）元组里面可以放多个元素。*与列表的区别：列表用方括号，元组用圆括号。
# *元组和列表都可以通过索引，返回某个位置的元素
a = (1, 2, 3)
print(a[1])
b = [1, 2, 3]
print(b[1])

# 19_
# 字典用于储存键值对："键:值" / "key:value"。键有对应的值，键是用来查找值的。
example_dictionary = {"小明": "13700000000",
                      "小花": "13700000001"}
# !键的类型必须是不可变的。
# !值的类型可以是可变的也可以是不可变的，所以值的类型可以是列表或者字典。

# 一、针对字典的方法
# 1 .在字典名后面跟方括号，获取某个键的值
xiaoming_tel = example_dictionary["小明"]
# zhangwei_tel = example_dictionary2[("张伟", 33)]

# 2.添加键值对/更新值 *取决于这个键是否已存在于字典
example_dictionary["小刚"] = "18600000000"
example_dictionary["小花"] = "18600000001"

# 3.删除键值对 *键本身不存在会报错
del example_dictionary["小明"]

# 4.获取某个键是否已经存在于字典中，“键 in 字典”会返回一个布尔值
print("小明" in example_dictionary)

# 5.dict.items()返回键值对(键值对组成元组)，dict.keys()返回键，dict.values()返回值
# *字典放入if语句或for语句时，默认返回键
# !for key, value in dict.items():
# 可以将字典里的键赋值给key,字典里的值赋值给value

# 6.字典可以通过len函数，得到字典里有多少键值对
len(example_dictionary)

# 二、一些尝试
# 1.字典也可以重新被赋值
# slang_dict = {1: 1, 2: 2}
# 2.可以打印列表，字典
# print(slang_dict)
# 3.sorted(字典名) 会对字典中的键排序并返回键。sorted()一般按照ASCII排序，对中文排序按照Unicode，所以看起来顺序杂乱。
# print(sorted(slang_dict))
# 4.键值对中键的类型必须是不可变的; 而值的类型是可变的，所以值的类型除上述外还可以是list, dictionary
# slang_dict[1] = {3: 3}
# print(type(slang_dict[1]))


# 结合input、字典、if判断，做一个查询流行语含义的电子词典程序
slang_dict = {'觉醒年代': '《觉醒年代》首次以电视剧的形式回溯中国共产党的孕育和创立过程，生动再现中国近代历史的大变局，'
              '深刻讲述中国人民是怎样选择了中国共产党。该剧播出后广受好评，成为党史学习教育的生动教材。',
              'YYDS': '“永远的神”的拼音缩写，用于表达对某人的高度敬佩和崇拜。2021年东京奥运会期间，不管是杨倩夺得首金，'
              '还是全红婵一场决赛跳出三个满分，或是“苏神”站上百米决赛跑道，全网齐喊“YYDS”，奥运期间一度刷屏。'}
slang_dict[
    '双减'] = '指进一步减轻义务教育阶段学生作业负担和校外培训负担。其目标是使学校教育教学质量和服务水平进一步提升，作业布置更加科学合理，' \
    '学校课后服务基本满足学生需要，学生学习更好回归校园，校外培训机构培训行为全面规范。'
# 此处在值中间换行由于没有花括号，需加\。
# *以上两个语句，反映了PEP8代码风格，即当括号内参数很多，需要换行编写的时候。
# 要么第一行放入参数，换行的参数与上一行的括号对齐；要么第一行不放入参数，即第一行最后字符是(，换行后有一个缩进
slang_dict['破防'] = '原指在游戏中突破了对方的防御，使对方失去防御能力。现指因遇到一些事或看到一些信息后情感上受到很大冲击，内心深处被触动，心理防线被突破。'
slang_dict['元宇宙'] = '源于小说《雪崩》的科幻概念，现指在XR（扩展现实）、数字孪生、区块链和AI（人工智能）等技术 '\
                       '推动下形成的虚实相融的互联网应用和社会生活形态。现阶段，元宇宙仍是一个不断演变、不断发展的概念。' \
                       'Facebook（脸书）对外公布更名为“Meta”，该词即来源于“Metaverse”（元宇宙）。'
slang_dict['绝绝子'] = '该词流行于某网络节目，节目中一些粉丝用“绝绝子”为选手加油。多用于赞美，表示“太绝了、太好了”。这个词引发了网友对网络语言的关注和讨论。'
slang_dict['躺平'] = '该词指人在面对压力时，内心再无波澜，主动放弃，不做任何反抗。' \
                     '“躺平”更像是年轻人的一种解压和调整方式，是改变不了环境便改变心态的自我解脱。短暂“躺平”是为了积聚能量，更好地重新出发。'
slang_dict['伤害性不高，侮辱性极强'] = '一段网络视频中，两名男子相互夹菜，而同桌的另一名女子则显得很孤单。于是有网友调侃“伤害性不高，侮辱性极强”。' \
                                      '后被网友用来调侃某事虽然没有实质性危害，但是却令人很难堪。'
slang_dict['我看不懂，但我大受震撼'] = '源自导演李安在纪录片《打扰伯格曼》（2013）里评价一部影视作品的话。现多用于表示自己对某件事情的不解、震惊。'
slang_dict['强国有我'] = '源自建党百年天安门广场庆典上青年学子的庄严宣誓。“请党放心，强国有我”是青年一代对党和人民许下的庄重誓言，' \
                         '彰显着新时代中国青年的志气、骨气、底气。'

query = input("请输入您想查询的流行语：")
if query in slang_dict:
    print("您查询的" + query + "含义如下")
    print(slang_dict[query])  # 列表通过排序作为索引查找元素，而字典可以通过键查找值
else:
    print("您查询的流行语暂未收录")
    print("当前本词典收录的词条数为：" + str(len(slang_dict)) + "条。")  # 返回dict中键值对数量

print(slang_dict[['YYDS', '觉醒年代']])
