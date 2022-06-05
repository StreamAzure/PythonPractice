# 练习1：华氏温度转换为摄氏温度。
# 提示：华氏温度到摄氏温度的转换公式为：C = (F-32)/1.8。
f = float(input("请输入华氏温度："))
c = (f-32)/1.8
print("摄氏温度为：%.1f" % c)

# 练习2：输入圆的半径计算计算周长和面积。
pi = 3.14
r = float(input("请输入圆的半径"))
S = (r**2)*pi
print("圆的面积为%.1f" % S)

# 练习3：输入年份判断是不是闰年。
year = int(input("请输入年份"))
judge = year % 4 == 0 and year % 100 !=0 or \
    year % 400 == 0
print(judge)