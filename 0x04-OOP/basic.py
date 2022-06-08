"""
类与对象基础
"""
class Student(object):
    # 构造函数，C++/Java中构造函数名与类名同名，而python统一为__init__ 
    # 没有专门的属性声明的地方，都写在__init__里面
    def __init__(self, name, age, foo): 
        self.name = name
        self.age = age 
        self.__foo = foo 
        # Python规定两个下划线开头的变量为private变量
        # 然而实际上通过特殊的变量名仍可以访问到这个变量，并不严格private
    
    # 参数列表中总有个self，即对象自己
    def study(self, course_name):
        print('%s正在学习%s' % (self.name, course_name))
    
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看成年人可以看的.' % self.name)

"""
@property装饰器
在Java中的通常做法是，属性全部private，但有public的setter和getter方法
对应到python中，就是将变量名以_开头，以属性名为方法名，对于getter方法加上@property，对于setter方法加上@xxx.setter

__slots__
在Python中，类的属性和方法是可以在程序运行时更改的，如果想限制绑定的属性，需要__slots__
只对该类有效，对其子类无效
"""
class Person(object):

    __slots__ = ('_name', '_age', '_gender') # 限定Person只有这三个属性

    def __init__(self,name,age):
        self._name = name # 属性以_开头暗示受保护
        self._age = age
    
    @property # getter方法装饰器
    def name(self): # 以属性名为方法名
        return self._name

    @property
    def age(self):
        return self._age
    
    @age.setter # 在此之前要先有getter方法
    def age(self, age):
        self._age = age

"""
静态方法 @staticmethod
"""
class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

def test():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c): # 与Java相同，直接通过类名调用静态方法
        t = Triangle(a, b, c)

"""
继承与多态
"""
from abc import ABCMeta, abstractclassmethod, abstractmethod 

class Human(object, metaclass=ABCMeta): # 将Human定义为抽象类
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @abstractmethod # 定义抽象方法
    def me(self):
        """自称"""
        pass


class Man(Human): # 括号内即继承的父类
    def __init__(self, name, age, grade):
        super().__init__(name, age) # 通过super().调用父类方法
        self._grade = grade

    def me(self): # 重写父类的抽象方法
        return "俺"

class Woman(Human):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    def me(self): # 重写父类的抽象方法
        return "わだし"

if __name__ == '__main__':
    w = Woman("小红",18,100)
    m = Man("小明",18,100)
    print("小红自称%s" % w.me())
    print("小明自称%s" % m.me())
