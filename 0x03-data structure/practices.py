import os
import time

def p1():
    content = '明明我喜欢你'
    while True:
        os.system('cls')
        print("⭐⭐⭐⭐⭐⭐⭐⭐")
        print("⭐",end="")
        print(content,end="")
        print("⭐")
        print("⭐⭐⭐⭐⭐⭐⭐⭐")
        time.sleep(0.2)
        content = content[1:] + content[0]
        # content[1:]即去掉了首个元素的列表

def p2():
    """
    《幸运的基督徒》
    有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
    有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，
    报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，
    15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
    """
    persons = [True] * 30
    counter, num, i = 30, 0, 0
    while counter > 15:
        if persons[i]:
            num += 1
            if num == 9:
                persons[i] = False
                counter -= 1
                num = 0
        i += 1
        i %= 30
    for x in persons:
        if x:
            print("√ ",end="")
        else:
            print("× ",end="")

if __name__ == '__main__':
    p2()

