"""
type()查看变量类型
"""
a = 1000
b = 12.343
c = "hello"
e = True
print(type(a))

"""
input()键盘输入
print()屏幕输出格式化字符串
"""
a = int(input('a = ')) 
# input的参数是输入提示文字，返回值是字符串，因此需要强制转换
b = int(input('b = ')) 
print('%d + %d = %d' % (a, b, a + b))
# 整数占位符%d，小数占位符%f

"""
身份运算符 `is` `is not` 判断两个数据引用对象是否一致
切片 `[:]`
逻辑运算符 `and` `or` `not`
"""
x = 5
y = 5
print(x is y) # 输出为True

"""
for-in 循环

range的参数是左闭右开的区间
range(101): 等价于for(int i = 0; i < 101; i++)
range(1,101)：等价于for(int i = 1; i < 101; i++)
range(1,101,2)： 等价于for(int i = 1; i < 101; i+=2)
range(100, 0,-2): 等价于for(int i = 100; i > 0; i-=2)
"""
# 实现1~100的求和
sum = 0
for x in range(101): # x 代指循环过程中的每一个元素，随便叫啥都可以
    sum += x
print(sum)

"""
while 循环
猜数字游戏
"""
import random
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print("猜小了")
    elif number > answer:
        print("猜大了")
    else:
        print("猜中了！")
        break
print("你猜了%d次" % counter)