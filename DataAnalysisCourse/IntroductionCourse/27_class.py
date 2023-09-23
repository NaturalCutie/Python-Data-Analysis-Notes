# 27_创建类
# *类和函数都是：定义的时候，里面的代码不会被执行；只有在调用的时候，才是里面的代码被实际执行的时候。

# 一、创建类
# 1.类有一个特殊的方法叫构造函数，主要作用是定义实例对象的属性，必须要被命名为"__init__"
# 2.括号里可以放任意数量的参数，
# 但第一个参数永远是被占用的，得用于表示对象自身，约定俗成叫"self",它能帮你把属性的值绑定在实例对象上
# *和定义普通变量时的下划线命名法不同，Python在定义类名的时候，用的是Pascal命名法，特点是用首字母大写来分隔单词
class CuteDog:
    def __init__(self):
        self.name = "Lambton"
        # 若每个对象的属性都有一样的初始值，可以用这种方式定义类的属性并赋值
        name = "Lambton"
        # Python认为只是在给普通的name变量赋值,且是局部变量


# 二、创建对象
# 1.创建对象是用类名，括号，里面放入参数，这样__init__方法就会被调用，并返回一个对象
# ！"self"参数是不需要手动传入的
# 2.获取对象的属性用"对象.属性名"来获取
dog1 = CuteDog()
print(dog1.name)
# 返回dog1对象所绑定的name属性的值，为Lambton


# 另：给__init__更加灵活的属性赋值，比如从参数获取属性的值
# 那创建对象时，就需要在括号里面传入属性的值，此处name属性的值被赋值为传入的cat_name参数的值
class CuteCat:
    def __init__(self, cat_name, age, color):
        self.name = cat_name
        # 属性名和参数名不一定一致
        self.age = age
        # self.age是绑定到对象身上的属性，而age是普通的变量，它的值是通过参数传进来的
        self.color = color



cat1 = CuteCat("jojo", 2, "橙色")
print(f"小猫{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}")
