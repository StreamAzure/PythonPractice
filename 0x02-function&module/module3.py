def foo():
    pass

def bar():
    pass


# 只有当本文件被Python解释器直接执行时才执行的部分
# 直接被Python解释器执行的模块都叫__main__
# 否则只执行被调用的函数
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()