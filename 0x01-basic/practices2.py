"""
练习1：百分制成绩转换为等级制成绩。
要求：如果输入的成绩在90分以上（含90分）输出A；
80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；
60分-70分（不含70分）输出D；
60分以下输出E。
"""
score = float(input("请输入百分制成绩："))
if (score >= 90):
    print("A")
elif (score >= 80):
    print("B")
elif (score >= 70):
    print("C")
elif (score >= 60):
    print("D")
else:
    print("E")

"""
输入两个正整数，计算它们的最大公约数和最小公倍数
"""
x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if (x % factor == 0 and y % factor == 0):
        print("x和y的最大公约数为：%d" % factor)
        print("x和y的最大公倍数为: %d" % (x * y // factor))
        break