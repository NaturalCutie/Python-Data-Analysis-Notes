# 2.2 安装Jupyter Notebook
# 1.定义
# Jupyter Notebook是一个基于网页的交互式计算环境，是数据分析、数据科学，甚至机器学习领域里非常流行的一款工具。
# 可以用来编写代码、运行代码、查看输出、可视化数据，并分享输出的报告文档
# 2.优点
# 1）Jupyter Notebook可以按单元格运行代码
# 对于搞数据的人来说，不是所有时候都想从头运行到结尾，
# 比如数据量特别大的时候，假如读取数据要等几秒，清洗数据要等几秒，
# 那在我们每次修改分析公式，想反复运行看效果的时候，不希望前面没有改动的步骤，比如说读取数据，还要反复被运行，因为这会浪费很多等待时间。
# 用Jupyter Notebook就很简单了，我们可以把不同步骤放在不同单元格里，每次运行一个单元格的代码，
# 这样我们可以只读取一遍数据，当反复修改和运行分析代码时，读数据的代码就不会再被运行了。
# 2）可展示的信息格式更丰富
# 我们用常规编辑器时，注释和代码一样都是纯文本，
# 但分析数据时，有时需要记录和解释更多东西，比如数据的北京、使用的公式、分析思路等等，
# 用Jupyter Notebook可以用Markdown标记语言，让注释更加清晰、有层次，还可以用LaTex插入公式
# 当你把Jupyter Notebook上的内容，以HTML等格式分享给其他人的时候，这些效果丰富的文字，也会原封不动地展示给对方，
# 帮助对方更好地理解你思考和分析的过程，也节约了你解答疑问的时间
# 3）交互式运行环境
# 交互模式相比命令行模式的好处是，当我们想查看输出的时候，不需要加上打印语句就能看到，
# 那我们就可以很方便地查看变量的值,输出中间结果，有利于快速探索数据，试验不同分析方法。
