# -*- coding  : utf-8 -*-
# @Time       : 2020/10/22 18：00
# @Author     : fei
# @File       : Homework1.py

"""
用类和面向对象的思想，“描述”生活中任意接触到的东西
（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
"""


# 定义电脑类
class Computer:

    def __init__(self):
        """初始化属性"""
        # 定义型号变量
        self.Model = 'Mac'
        # 定义运行内存变量
        self.Runme = '16g'
        # 定义内存变量
        self.Ram = '512g'
        # 定义电脑尺寸变量
        self.Size = '16'

    def Description(self):
        """
        描述我的电脑
        """
        print('我有一台{}, 尺寸: {}, 运行内存: {}, 内存: {}'.format(self.Model, self.Size, self.Runme, self.Ram))


# 定义游戏类
class Game:

    def __init__(self, Gamename, Grade):
        """初始化属性"""
        # 定义游戏名称变量
        self.Gamename = Gamename
        # 定义游戏登录
        self.Grade = Grade

    def Description(self):
        # 打印
        print('喜欢的游戏:{}, 等级:{}'.format(self.Gamename, self.Grade))


# 定义动物类
class Animal:

    def __init__(self, Anima, Habits):
        """初始化属性"""
        # 定义动物变量
        self.Anima = Anima
        # 定义动物习性登录
        self.Habits = Habits

    def Description(self):
        # 打印
        print('喜欢的动物:{}, 习性:{}'.format(self.Anima, self.Habits))


# 定义动物类
class Sport:

    def __init__(self, Sport):
        """初始化属性"""
        # 定义游戏名称变量
        self.Sport = Sport

    def Description(self):
        # 打印
        print('喜欢的运动:{}'.format(self.Sport))


# 继承动物类
class Sportzi(Sport):

    def Description(self):
        # 重写打印方法
        print('子类喜欢的运动:{}'.format(self.Sport))
