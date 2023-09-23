# 28_class2
# 一、创建方法
# 1.定义方法
# 1）写在class里面，前面有缩进
# 2）与__init__一样，第一个参数是"self"。
# ！一个作用是可以让我们在方法里面，去获取或修改和对象绑定的属性。
# 这样就实现了，方法调用结果，根据属性的不同而改变
# *方法的命名采用下划线命名法
# 2.调用类方法，
# 就用对象.方法名,括号里面放上参数进行调用
# ！"self"参数在这里也不需要手动传入的
class CuteCat:
    def __init__(self, cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

    def speak(self):
        print("喵" * self.age)
        # 字符串乘数字，表示把字符串重复这么多次

    def think(self, content):
        print(f"小猫{self.name}在思考{content}...\n")


cat1 = CuteCat("Jojo", 3, "橙色")
cat1.speak()
cat1.think("现在去抓沙发还是去撕纸箱")


# 定义一个学生类
# 要求
# 1.属性包括学生姓名、学号，以及语数英三科的成绩
# 2.能够设置学生某科目成绩
# 3.能够打印出学生的所有科目成绩
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade
        # 字典放入if语句或for语句时，默认返回键

    def print_grades(self):
        print(f"同学{self.name}(学号：{self.id})的成绩为：")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")


chen = Student("小陈", "100618")
zeng = Student("小曾", "100622")
zeng.set_grade("数学", 95)
zeng.set_grade("语文", 91)
zeng.print_grades()
