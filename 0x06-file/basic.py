"""
七种文件操作模式
'r' : 读取
'w' : 写入（原有的内容会被覆盖）
'x' : 写入（如果文件已经存在会产生异常）
'a' : 追加（将内容写入到已有文件的末尾）
'b' : 二进制模式
't' : 文本模式
'+' : 更新（既可读又可写）
"""

import time


def read_file(path):
    f = None
    try:
        f = open(path, 'r', encoding = 'utf-8')
        print(f.read())
    except FileNotFoundError:
        print("无法打开指定的文件！")
    except LookupError:
        print("指定了未知的编码！")
    except UnicodeDecodeError:
        print("读取文件时解码错误！")
    finally:
        if f:
            f.close()

"""
使用with关键字来自动释放文件资源
"""
def read_file2(path):
    with open("致橡树.txt", 'r', encoding='utf-8') as f:
        print(f.read()) # 一次性读取全部内容

    with open("致橡树.txt", mode = 'r', encoding='utf-8') as f:
        for line in f: # 逐行读取
            print(line, end='')
            time.sleep(0.5)
    print()
    
    with open("致橡树.txt", encoding='utf-8') as f:
        lines = f.readlines() # 逐行读入到列表
    print(lines)

"""
写入到文件
"""
from math import sqrt


def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成!')

"""
二进制文件的读写
"""
def copy_image():
    try:
        with open('test.png', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('头像.png', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('图片复制结束.')

"""
以JSON格式保存到文件中
json.dump()
"""
import json

def save_data():
    mydict = {
        'name': '阿川',
        'age': 18,
        'qq': 957658,
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('阿川的data.json', 'w', encoding='utf-8') as f:
            json.dump(mydict, f)
    except IOError as e:
        print(e)
    print('保存数据完成!')

if __name__ == '__main__':
    save_data()