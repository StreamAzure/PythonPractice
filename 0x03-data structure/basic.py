import sys
"""
列表 []
"""
# 定义列表
list1 = [1,3,7,100]
print(list1)

# 重复列表元素
list2 = ['we']*3
print(list2)

# 获取列表中的元素个数
print(len(list1))

# 下标（索引）
print(list1[0])
print(list1[-1]) # 负值表示从后往前数，如-1表示列表最后一个元素

# 遍历列表元素
for i in range(0, len(list1)): # 相当于 for(int i = 0; i < list1.length(); i++)
    print(list1[i])

# 遍历列表，同时获取下标与元素值
for i, elem in enumerate(list1):
    print(i, elem)

# 向列表末尾追加元素 append
list1.append(114514)
print(list1)

# 向列表指定下标插入元素 insert
list1.insert(1, '我是新来的')
print(list1) # [1, '我是新来的', 3, 7, 100, 114514]

# 列表合并
list1 += list2
print(list1) # [1, '我是新来的', 3, 7, 100, 114514, 'we', 'we', 'we']

# 判断元素是否在列表中，若是则删除 remove
if '我是新来的' in list1:
    list1.remove('我是新来的')

# 对列表指定下标删除元素，并打印该元素 pop
# 与remove的区别是，remove没有返回值，而pop有返回值，为被删除的元素
print(list1.pop(-1))

# 清空列表元素 clear
list1.clear()
print(list1) # []

# 列表切片
grades = [98,78,45,24,14]
grade1 = grades[1:4] # [78, 45, 24]
# [1:4]格式与range(1,4)类似，左闭右开，表示取下标≥1且＜4的元素
print(grade1)

grade2 = grades[:] # [98, 78, 45, 24, 14]
# 相当于复制列表
print(grade2)

grade3 = grades[::-1] # [14, 24, 45, 78, 98]
# 反转列表
print(grade3)

# 列表排序
list1 = [15,156,4,544,54]
list2 = sorted(list1) # sorted函数不改变传入的列表，而是拷贝并排序然后返回
print(list2)

# 指定降序排列
list3 = sorted(list1, reverse=True) 
print(list3)

# 指定按字符串长度升序排列。默认按字典序升序排列
list4 = ['app','appjijo','jojij','ajlj']
list5 = sorted(list4, key=len) 
print(list5)

# 直接对原列表进行排序，调用其自身的sort方法即可
list1.sort(reverse=True)
print(list1)

"""
生成式和生成器
快速地按照指定规则创建列表
"""
# 对于下述方式，f中的每一个元素都被实际创建了，因此也实际地占用了内存，但访问时不需要计算
f = [x for x in range(1, 100)]
print(f) # 920
print(sys.getsizeof(f))

# 下述方式只创建了生成器对象，其中元素只在真正访问的时候才会被计算出来，额外耗时但节省了内存
f = (x for x in range(1, 100))
print(sys.getsizeof(f)) # 112
print(f) # <generator object <genexpr> at 0x0000024274B4FF20>
for val in f:
    print(val)
print(sys.getsizeof(f)) # 还是112

# 将一个函数改造成生成器函数，关键字yield
# 例：生成斐波那契数列
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a # 定义列表中的一个元素

for val in fib(20): # 把整个函数当成列表来用
    print(val)

"""
元组 ()
不可修改，不可重新赋值
"""
# 定义元组
t = ('你好','1','我是')

# 重新定义元组，实际上是产生了新的元组，原来的被垃圾回收
t = ('不好')

# 元组转列表
list1 = list(t)
print(list1)

# 列表转元组
t1 = tuple(list1)
print(t1)

"""
集合 {}
与数学定义上的集合一致，不允许重复元素
"""
# 定义集合
set1 = {1,2,3,4,4,4,4,4}
print(set1)

# 构造器
set2 = set(range(1,10))
set3 = set((1,2,3,4))
print(set3)

# 生成式
set4 = {x for x in range(1, 100) if x % 3 == 0} 
# 虽然按道理来讲应该会是升序排列的，但事实上当范围比较大的时候会乱掉
print(set4)

# 添加元素
set1.add(6) # 末尾追加1个元素
print(set1)
set1.update([11,12]) # 末尾追加多个元素
print(set1)

# 删除元素
set1.discard(4) # 删除指定值的元素（不是下标！）
print(set1)
set1.pop() # 删除首个元素，返回值为这个元素
print(set1)

# 集合的交集、并集、差集、对称差运算
print(set1 & set2) # 交集
print(set1 | set2) # 并集
print(set1 - set2) # 差集
print(set1 ^ set2) # 对称差

"""
字典
每个元素都为一个key和一个value构成的键值对，冒号分开
"""
# 定义字典
number = {'Amy': 1, 'John' : 2, 'Mike' : 3}
print(number)

# 构造器
dic1 = dict(one=1, two=2, three=3)
print(dic1)

# zip函数将两个序列捆成字典
dic2 = dict(zip(['a','b','c'],'123'))
print(dic2)

# 生成式
dic3 = {x : x ** 2 for x in range(1, 10)}
print(dic3)

# 遍历字典
for key in dic3:
    print(f'{key}: {dic3[key]}')

# 删除字典中的键值对
print(dic3.popitem())

# 清空字典
dic3.clear()
print(dic3)