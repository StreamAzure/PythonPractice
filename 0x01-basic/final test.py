"""
测试1：输出所有的水仙花数
水仙花数是一个3位数，它的每个位数字的立方之和等于它本身
"""
for x in range(100,1000):
    x1 = x
    sum = 0
    while(x1 > 0):
        sum += (x1 % 10)**3
        x1 //= 10
    if(sum == x):
        print("%d 是水仙花数" % x)

"""
测试2：输出斐波那契数列的前20个数
斐波那契数列：f(1)=f(2)=1, f(x)=f(x-1)+f(x-2)
"""
pre1 = 1
pre2 = 1
for x in range(1, 21):
    if(x == 1 or x == 2):
        print("1")
    else:
        k = pre1 + pre2
        print("%d" % k)
        pre1, pre2 = pre2, k

"""
测试3：输出100以内的所有素数
"""
for x in range(2, 101):
    k = True
    for i in range(2, x):
        if (x % i == 0):
            k = False
            break
    if(k):
        print("%d 是素数" % x)
    