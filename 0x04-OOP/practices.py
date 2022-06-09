from abc import ABCMeta, abstractmethod
from random import randint, randrange
import time

class Fighter(object, metaclass=ABCMeta):
    """玩家"""
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
    
    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @hp.setter
    def hp(self, hp):
        self._hp = hp
    
    @property
    def isAlive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """
        :param othter: 被攻击的对象
        """ 
        pass

class Player(Fighter):
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name,hp)
        self._mp = mp
    
    def attack(self, other):
        other.hp -= randint(15, 25)
    
    def magic_attack(self, other):
        if self._mp >= 20:
            self._mp -= 20
            other.hp -= randint(10, 15)
            return True
        else:
            return False
    
    def __str__(self):
        return '\n=== 玩家 %s ===\n' % self._name + \
            'HP: %d\n' % self._hp + \
            'MP: %d\n' % self._mp

class Monster(Fighter):
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '=== 怪物 %s ===\n' % self._name + \
            'HP: %d\n' % self._hp

def display_info(p,m):
    print(p)
    print(m)

def main():
    p1 = Player("阿川", 1000, 120)
    m1 = Monster("哥布林", 250)
    fight_round = 1
    while p1.isAlive and m1.isAlive:
        time.sleep(0.5)
        print('==== 第 %02d 回合 ====' % fight_round)
        skill = randint(1, 10)
        if skill <= 6: # 60%概率使用普通攻击
            print('%s 使用普通攻击打了 %s' % (p1.name, m1.name))
            p1.attack(m1)
        elif skill <= 9:
            if p1.magic_attack(m1):
                print('%s 使用魔法攻击打了 %s' % (p1.name, m1.name))
            else:
                print('%s 使用魔法攻击失败' % p1.name)
        time.sleep(0.5)
        if m1.isAlive:
            print('%s 使用普通攻击打了 %s' % (m1.name, p1.name))
            m1.attack(p1)
        time.sleep(0.5)
        display_info(p1, m1)
        fight_round += 1
    print("\n==== 战斗结束 ====\n")
    time.sleep(0.2)
    if p1.isAlive:
        print("玩家胜利!")
    else:
        print("怪物胜利！")

if __name__ == '__main__':
    main()