# 2.3 Jupyter Notebook使用
# Jupyter Notebook会是我们数据分析中使用的核心工具

# 一、启动Jupyter Notebook
# 1.1）Windows系统，在菜单栏搜索CMD，点击命令提示符
# 2）macOS系统，点击顶部菜单栏的放大镜，输入"终端"或"terminal"，回车进入
# 出现大黑窗口后，输入Jupyter Notebook的启动命令："Jupyter-Notebook"
# 这时默认浏览器会自动打开一个网页，展示Notebook的主面板。
# 2.如果不小心关闭了JN的网页，地址可以再CMD或终端里找到，
# 其中某一行："The Jupyter Notebook is running at...",后面跟着的就是页面地址，复制到浏览器即可
# *3.接下来的时间里，记得不要关闭这个输入了启动命令的CMD或终端，否则JN会被终止

# 二、创建Jupyter Notebook文件
# 1.创建文件
# 希望文件在什么位置，就点进那个文件夹，然后点击New，Notebook，
# 一个新的编辑界面就会被打开，而且在桌面上也能看到一个全新的文件出现了
# 2.重命名文件
# 在编辑界面，点下标题，输入想要的名字

# 三、Jupyter Notebook编辑界面
# 标题下面分别是菜单栏、工具条以及单元格，
# 工具条就是把菜单栏里一些最常用的操作摆出来，所以大部分时候我们只需要通过工具条和单元格打交道
# 单元格主要用来写Python代码和文字，

# (一)、编辑模式和命令模式
# 1.编辑模式
# 在我们点击单元格里面后，外框会变成绿色，表示当前是编辑模式，
# 2.命令模式
# 完成输入后，点Esc键，或者鼠标点下其它地方，外框会变成蓝色，表示当前是命令模式

# (二)、工具栏
# 1.第一个按钮，表示保存文件内容
# 2.第二个加号按钮，表示在当前选中的单元格下面，新建一个单元格，
# 3.接下来三个按钮，分别表示剪切选中的单元格、复制选中的单元格，以及粘贴选中的单元格
# 还可以按住Shift键选中多个单元格，然后同一进行操作，
# 4.上箭头表示把选中的单元格往上移动一格，下箭头表示往下移动一格，来更改单元格顺序
# 5.运行按钮
# 会执行这个单元格里面所有Python代码,
# 1）执行时，左边方括号会展示星号，表示正在运行，
# 2）执行完毕后，方括号里面会变成数字，
# 3）数字表示的是执行顺序，比如运行完第一个单元格后，旁边数字显示1；继续运行下一个单元格，旁边数字就会显示2。
# 4）JN很灵活的一点是，你可以用任意顺序运行单元格，
# 比如可以运行第三格后，回到第一格再执行一遍；也可以多次反复运行同一个单元格。旁边的数字，会帮忙记录和告知执行过的顺序
# 5）顺序是很关键的，
# 比如你分别在第二和第三个单元格里，写了读取和查看数据的代码，想要修改读取的文件，需要修改和再次运行读取数据的代码
# 这时，第二个单元格的数字大于第三个单元格，就能侧面提醒我们，第二个单元格里，查看数据来输出的代码还没有被更新，查看的还是之前的数据文件。
# 所以应该把第三个单元格也运行一次
# 另：代码单元格里的代码是通过交互模式运行的，也就是说可以不需要print语句，就能直接看到执行输出的结果，
# *但是如果单元格里有多条输出语句，只有最后一项的输出会被展示，我们还是要借助print，才能同时展示多项输出结果，
# 6.终止执行按钮
# 执行单元格里代码的过程中，想要中断的话，就可以点击它
# 7.重启按钮
# 这会帮我们清空所有定义过的变量，而且单元格旁边的数字也会重新从1开始，表明重启过
# 举个例子，假如第一格定义了一个变量，第二格输出这个变量的值，那运行第一格后变量的值就已经被储存到内存里了，每次输出第二格就会输出对应的值；
# 但重启后，再运行第二格，就会提醒我们变量不存在了。
# 8，重启并重新运行所有单元格的按钮
# 非常使用，如果你想看自己写的所有代码，从上往下完整执行一遍的输出，就用这个操作
# 它可以帮我们检查单元格顺序是否有问题
# 9.下拉框，可以让我们切换单元格里的内容。最常用的就是代码和Markdown，单元格并不限于写代码，也可以写文字
# 1）Markdown
# 是一种帮助我们为内容增加样式的标记语言，语法简单
# 通过在前面添加1~6个#和1个空格，可以把文字设置成一至六级标题
# 2)公式
# a.在行内插入公式，就用1个美元符号，包裹住那个公式
# b.要插入一个独占一行的公式，就用2个美元符号，包裹住那个公式
# c.复杂的公式，可以用LaTex语法来表示
# 10.键盘按钮，是快捷键配置，
# 掌握快捷键的使用，可以大大提升我们使用JN的效率，*在命令模式下使用
# 1）A键，可以在当前单元格上方插入一个新的单元格
# 2）B键，可以在当前单元格下方插入
# 3）连按两次D，可以删除当前选中的单元格
# 4)Shift+Enter，运行当前单元格，并跳到下一个单元格

# 四、分享Jupyter Notebook
# 1.可以自行编辑和运行
# 如果对方使用JN，可以把这个以.ipynb为后缀的文件，直接发给对方
# 2.只读
# 点击File，选择Save and Export Notebook as，有很多选项
# 比如HTML，这是针对网页的标记语言，所以对方可以直接用浏览器打开，所有代码以及Markdown文字都会原封不动得展示出来

# 五、打开之前创建过的Jupyter Notebook
# 启动JN,进入存放notebook的目录，点击.ipynb的文件
