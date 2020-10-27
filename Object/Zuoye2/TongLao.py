"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，

see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
"""


# 定义童姥类
class TongLao:

    def __init__(self, power):
        self.my_hp = 1000
        self.my_power = power

    def see_people(self, name):
        if name == 'WYZ' or name == '无崖子':
            print('师弟！！！！')
        elif name == '李秋水':
            print('师弟是我的！')
        elif name == '丁春秋':
            print('叛徒！我杀了你')
        else:
            print('无此人')

    def fight_zms(self, enemy_hp, enemy_power):
        """
        天山折梅手方法，将自己的武力值提升10倍，血量缩减2倍
        :param enemy_hp: 敌人hp
        :param enemy_power: 敌人武力值
        :return:
        """
        # hp减半
        self.my_hp //= 2
        # 武力值提示10倍
        self.my_power *= 10
        # 对打
        self.my_hp -= enemy_power
        enemy_hp -= enemy_power

        # 判断输赢
        if self.my_hp > enemy_hp:
            print('我赢了！')
        elif self.my_hp == enemy_hp:
            print('平手！')
        else:
            print('我输了！')
