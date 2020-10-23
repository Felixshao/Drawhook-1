# -*- coding: utf-8 -*-
# @Time     :2020/10/22 18：00
# @Author   :fei
# @File     :game.py

import random

my_num = 0  # 失败次数
enemy_num = 0   # 失败次数


def game(num=0):
    """
    # 对敌游戏，3回合
    :param num:回合数
    :return:
    """
    global my_num, enemy_num    # 全局变量
    print('')   # 换行
    my_hp = 1000     # 定义初始血量
    enemy_hp = 1000  # 定义初始血量

    my_power = random.randint(10, 200)      # 定义随机攻击值
    enemy_power = random.randint(10, 200)   # 定义随机攻击值

    while True:
        if my_num == 2 and enemy_num == 2:  # 失败次数都为2次时，平手
            print('平手')
            break
        elif my_num == 2:
            print('我输了')
            break
        elif enemy_num == 2:
            print('我赢了')
            break

        my_hp = my_hp - enemy_power      # 攻击并统计血量
        enemy_hp = enemy_hp - my_power   # 攻击并统计血量

        print('第{}回合，我的血量：{}, 敌人的血量：{},'.format(num+1, my_hp, enemy_hp))    # 输入每次攻击后血量

        # 判断双方最后谁的血量小于等于0
        if my_hp <= 0 and enemy_hp <= 0:
            my_num += 1     # 失败次数加1
            enemy_num += 1
            game(my_num)    # 回调进入下一回合
            break   # 结束后退出
        elif my_hp <= 0:
            my_num += 1
            game(my_num+enemy_num)
            break
        elif enemy_hp <= 0:
            enemy_num += 1
            game(my_num+enemy_num)
            break


if __name__ == '__main__':
    # 调用游戏方法
    game()