# 29_类继承
# 继承是在说：面向对象编程允许创建有层次的类，即类可以有子类和父类，来表示从属关系
# 这样做的好处是父类的属性、方法都可以被继承，不需要反复定义，减少代码的冗余

# 1.创建一个父类，把共享的属性和方法全部挪进去
# 在子类名后面加上括号，里面写上父类的名字
# 2.调用方法时，优先看所属的类有没有该方法，没有的话，往上找父类的同名方法用
# *同时有的话，只执行子类的方法
class Mammal:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.num_eyes = 2

    def breathe(self):
        print(self.name + "在呼吸...")

    def poop(self):
        print(self.name + "在拉屎...")


# *子类不用缩进
class Human(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        # 当子类之间方法有部分不同时，特别是部分属性值不同时，最好用super()
        # 可以省略重复的属性和方法代码行
        # super()会返回当前类的父类，如:super().__init__()会调用父类的构造函数
        # 子类方法中，缩进 + super().方法名(参数(省略(self)) + 方法不同的部分
        self.has_tail = False

    def read(self):
        print(self.name + "在阅读...")


class Cat(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        self.has_tail = True

    def scratch_sofa(self):
        print(self.name + "在抓沙发...")


cat1 = Cat("Jojo", "男")
print(cat1.name)
cat1.poop()


# 类继承练习：人力系统
# -员工分为两类：全职员工 FullTimeEmployee、兼职员工 PartTimeEmployee
# -全职和兼职都有"姓名 name"、"工号 id"属性
#  都具备"打印信息 print_info" (打印姓名、工号)方法
# -全职有"月薪 monthly_salary"属性
#  兼职有"日薪 daily_salary"属性、"每月工作天数 work_days"属性
# -全职和兼职都有"计算月薪 calculate_monthly_pay"的方法，但具体计算过程不一样
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"员工{self.name},工号:{self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        self.monthly_salary = monthly_salary
        super().__init__(name, id)

    def calculate_monthly_pay(self):
        print(f"{self.name}的月薪为：{self.monthly_salary}")


class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        monthly_salary = self.work_days * self.daily_salary
        print(f"{self.name}的月薪为：{monthly_salary}")


zheng = FullTimeEmployee("小郑", "2978", 50000)
zeng = PartTimeEmployee("小曾", "2979", 500, 30)
zheng.print_info()
zheng.calculate_monthly_pay()
zeng.calculate_monthly_pay()
