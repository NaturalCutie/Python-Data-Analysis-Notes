# 34_测试
# 测试的目的是帮我们确认，程序的行为是否和预期相同。
# 而且测试除了能帮我们验证新代码是否正确之外，还能验证在改动老代码之后，不该受影响的地方，也仍然会按预期进行

# 一、assert语句
# 1.assert后面可以跟上任何布尔表达式，也就是值为True或False的表达式。
# *测试时我们会在assert后面跟上，我们认为应该为True的表达式
# 2.如果assert后面的表达式，最终求值出来的结果为True，那么无事发生，继续运行后面的代码
# 但如果求值出来为False,就会产生"AssertionError"，即断言错误。相当于提醒运行程序的人，这里不符合预期
# 3.用assert的问题是，一旦出现AssertionError，程序就中止了。
# 后面的代码并不会运行，我们并不知道剩下的代码里有哪些其他问题.
assert len("Hi") == 2
# assert "a" in ["b", "c"]
# assert 1 + 2 > 6

# 所以一般我们测试会使用专门做测试的库，它们能一次性跑多个测试用例(TestCase)，
# 并且能更直观地展现哪些测试用例通过了，哪些没有。
# 另：测试用例(testcase)是独立的，即一个testcase实例的代码必须是完全自含的(不用调用此类的其它测试用例)

# 二、unittest库
# 1.unittest是一个很常用的Python单元测试库,是Python标准库
# 2.单元测试的意思是，对软件中的最小可测试单元进行验证，比如验证某函数某方面表现是否符合预期
# ！3.我们一般会划分测试代码和实现代码到独立文件里，而不是和要实现的功能混在一起。
# ！4.为了能调用要测试的功能，还要在测试文件里，把要测试的函数或类也引入进来，
# 如果测试文件和被测试文件位于同一文件夹下，用 from 文件名 import 函数名 或 from 文件名 import 类名
# *文件名不能以数字开头

# （一）、写测试
# 1.创建一个类，名字可以以Test开头，表示这是一个用来测试的类.
# 它要当unittest.TestCase的子类，这样就能使用那些，继承自unittest.TestCase的各种测试功能
# 2.在这个类下面可以定义不同的测试用例,每一个测试用例都是类下面的一个方法
# ！命名必须以"test_"开头，因为unittest这个库，会自动搜寻"test_"开头的方法，而且只把"test_"开头的当成测试用例
# 3.由于用assert，出现AssertionError，程序就直接中断了；
# 所以我们可以用unittest库里TestCase类的assertEqual方法
# 咱们的测试类已经继承自那个类，所以可以直接通过self调用父类方法
# 另：assertEqual方法用法：传入的第一个参数和第二个参数如果相等，显示测试通过；如果不相等，显示测试不通过，但程序也不会炸
# 4.写好测试用例后,我们只需要在编辑器的终端，输入"python -m unittest",表示运行unittest
# 这个库就会自动搜索所有，继承了unittest库里TestCase类的子类，运行它们所有以"test_"开头的方法，然后展示测试结果
# (终端可以输入，如：python -m unittest test_module,TestClass.test_method,运行文件、类和测试用例的测试
# 测试模块也可以通过文件路径指定： )
# 5.结果会告诉你共运行了几个测试，
# 然后上面的点点，每个点代表一个测试通过；如果有一个测试没有通过，其中一个点会变成F；如果一个测试出现异常，其中一个点会变成E
# unittest还会详细告诉你是哪个文件下的哪个方法造成了测试失败，以及为什么失败

# 例题在TestCases文件夹里


# 35_测试

# (二)、unittest.TestCase类的常见测试方法
# 1.assertEqual(A,B) 类似于 assert A==B
# 2.assertTrue(A) 类似于 assert A is True
# 3.assertIn(A,B) 类似于 assert A in B
# 4.assertNotEqual(A,B) 类似于 assert A!=B
# 5.assertFalse(A) 类似于 assert A is False
# 6.assertNotIn(A,B) 类似于 assert A not in B

# *本质上assertTrue 可以代替这些所有方法，
# 比如以下两个测试：都是在验证2是否不存在于[1, 2]这个列表里，通过与否的结果也是一样的
# *但还是推荐更具针对性的方法
# 比如想测试元素不在列表里，用assertNotIn这个专门针对元素和列表的方法，而不是assertTrue这个万能方法，
# 原因是在测试未通过的时候，更针对性的方法，会给出更详细的失败原因

# assertTrue(2 not in [1, 3 - 1])
# AssertionError: False is not true
# assertNotIn(2, [3 - 1])
# AssertionError: 2 unexpectedly found in [1, 2]

# (三)、其他方法
# 有些时候我们还可以通过额外方法，进一步提高测试效率

# setUp方法 *第一个字母s小写
# *假如我们要测试一个类,
# *为了能调用各种类方法，我们需要创建实例对象，由于不同测试用例之间是独立的，测试不同方法的时候，我们要不停创建新对象。
# 为了减少不必要的重复代码，我们可以利用TestCase类里的SetUp方法：
# 在运行各个测试方法，也就是"test_"开头的方法前，SetUp方法都会先被运行一次。
# 我们只需要在SetUp方法里，把测试对象创建好，*作为当前测试类的一个属性
# 然后在方法里，就可以通过属性，获取那个已创建好的对象，去写测试语句


# 实现代码sentence.py
class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    """返回句子字母数量"""
    def str_count(self):
        return len(self.sentence)

    """返回句子单词数量"""
    def word_count(self):
        return len(self.sentence.split(" "))

    """返回所有字母大写后的句子"""
    def upper(self):
        return self.sentence.upper()


# 原测试代码
import unittest
# from sentence import Sentence


class TestSentence1(unittest.TestCase):
    def test_str_count(self):
        sentence = Sentence("Hello World")
        # ！可以在其他方法内创建对象
        self.assertEqual(sentence.str_count(), 12)
        # ！方法调用也可以作为参数

    def test_word_count(self):
        sentence = Sentence("Hello World")
        self.assertEqual(sentence.word_count(), 2)

    def test_upper(self):
        sentence = Sentence("Hello World")
        self.assertEqual(sentence.upper(), "HELLO WORLD!")


# 运用setUp方法的测试代码
# import unittest
# from sentence import Sentence


class TestSentence2(unittest.TestCase):
    def setUp(self):
        self.sentence = Sentence("Hello World!")

    def test_str_count(self):
        self.assertEqual(self.sentence.str_count(), 12)

    def test_word_count(self):
        self.assertEqual(self.sentence.word_count(), 2)

    def test_upper(self):
        self.assertEqual(self.sentence.upper(), "HELLO WORLD!")

# 例题在TestCases文件夹里
