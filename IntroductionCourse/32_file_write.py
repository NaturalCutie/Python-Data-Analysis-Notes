# 32_文件操作|写文件
# 把程序输出结果储存为文件，就可以不用反复运行程序，也可以把结果轻松共享给他人
# 写文件和读文件有非常多相似之处，都需要打开文件，并且在操作完成后关闭文件

# 一、打开文件
# 1.第一个参数里放文件路径
# 2.第二个参数要传入模式
# 1）写入模式用“w”表示
# *写入模式下，如果文件路径不存在，程序就会自动创建，传入文件名的那个文件
# *如果文件路径已经存在，就会先把原本的文件内容清空
# 无法读文件，用read方法，程序会报错

# 2）附加模式，用"a"表示
# *附加模式下，如果文件路径不存在，程序就会自动创建，传入文件名的那个文件
# *如果文件路径已经存在，不把原本文件内容清空，可以在后面追加内容
# 无法读文件，用read方法，程序会报错

# 3）同时支持读写文件，用"r+"表示
# *在r+模式下，文件路径不存在的话，就会报一个叫FileNotFoundError的错误，提示文件不存在
# *此r+模式下，如果文件路径已经存在,从开始位置读取或者写入
# *读取或写入都是从当前位置开始
# 即先调用read方法，再调用write方法，从文件结尾附加写入
# 先调用write方法，再调用read方法。会先从文件开头位置边写入边覆盖已有内容，再从写入内容后，读取未被覆盖内容
# 先调用readline方法，再调用write方法，会先读一行文件，再从第二行开始边写入边覆盖

# 4）同时支持读写文件，用"a+"表示
# *a+模式下，如果文件路径不存在，程序就会自动创建，传入文件名的那个文件
# *此a+模式下，如果文件路径已经存在,从最后位置读取或者写入
# *读取或写入都是从当前位置开始

# 3.我们可以传入可选参数encoding，来确保写入的文件编码也是UTF-8

# 二、写文件
# 1.write方法


# 任务1：在一个新的名字为"poem.txt"的文件里，写入以下内容：
# 我欲乘风归去，
# 又恐琼楼玉宇
# 高处不胜寒。
with open("32_poem.txt", "w", encoding="utf-8") as f:
    f.write("我欲乘风归去，\n又恐琼楼玉宇，\n高处不胜寒。")

# 任务2：在上面的“poem.txt”的文件结尾处，添加以下两句：
# 起舞弄清影，
# 何似在人间。
with open("32_poem.txt", "a", encoding="utf-8") as f:
    f.write("\n起舞弄清影，\n何似在人间。")
