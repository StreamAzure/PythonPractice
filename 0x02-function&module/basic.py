"""
函数
"""
def add(a=0, b=0, c=0): # 在定义参数时可以设置默认值
    return a + b + c

print(add(1)) # 可以缺省参数
print(add(1,2))
print(add(1,2,3))
print(add(c=2,a=1,b=2)) # 可以不按顺序给参数

"""
函数中的可变参数
"""
def add(*args): # 加*号表示这是个可变参数
    total = 0
    for val in args:
        total += val
    return total

print(add())
print(add(1))
print(add(1,2,3,4,5))

"""
注意，Python中没有函数重载的概念，同名函数中的后者会覆盖前者
使用模块区分同名函数
"""
from module1 import foo as f1
from module2 import foo as f2
f1()
f2()

"""
变量的作用域
不在任何一个函数中定义的变量为全局变量
在函数中定义的变量为局部变量
要在函数中修改全局变量，需要加global标识符
"""
def modify():
    global a # 如果全局作用域中没有a，则本行代码将定义一个全局变量a
    a = 200
    print(a) # 200

if __name__ == '__main__':
    a = 100
    modify()
    print(a) # 200

"""
尽量少用全局变量
"""