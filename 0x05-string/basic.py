"""
字符串
"""
s1 = 'hello'
s2 = "hello"
s3 = """
hello,
world!
"""
print(s1,s2,s3,end='')

"""
`\`符号用于转义
如果希望直接显示它，可以写成`\\`或在字符串前加上`r`
"""
s1 = r'\hello' # \hello
s2 = '\\hello' # \hello
print(s1, s2)

"""
字符串切片
"""
s1 = "hello" * 3
print(s1) # 重复

s2 += s1 
print(s2) # 拼接

print('ll' in s1) # 判断是否包含指定子串

str3 = '123456789'
print(str3[2:5]) # 左闭右开 345
print(str3[::-1]) # 翻转

"""
字符串常用方法
"""
str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 13

# 获得字符串首字母大写的拷贝 .capitalize
print(str1.capitalize()) # Hello, world!

# 获得字符串每个单词首字母大写的拷贝 .title
print(str1.title()) # Hello, World!

# 获得字符串变大写后的拷贝 .upper
print(str1.upper()) # HELLO, WORLD!

# 从字符串中查找子串所在位置 .find
print(str1.find('or')) # 8
print(str1.find('shit')) # -1

# 与find类似但找不到子串时会引发异常 .index
# print(str1.index('or'))
# print(str1.index('shit'))

# 检查字符串是否以指定的字符串开头 
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True

# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True

# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))

# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'

# 检查字符串是否由数字构成
print(str2.isdigit())  # False

# 检查字符串是否以字母构成
print(str2.isalpha())  # False

# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)

# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())

"""
字符串格式化输出
"""
# 法一：以{序号}作为占位符，后加.format()
a, b = 5, 10
print('{0} * {1} = {2}'.format(a,b,a*b))

# 法二：Python 3.6以后，直接在字符串前加f，{}里写变量名
print(f'{a} * {b} = {a * b}')