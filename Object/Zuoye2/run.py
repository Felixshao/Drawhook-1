from Object.Zuoye2.XuZhu import XuZhu


if __name__ == '__main__':

    wx = XuZhu(100)
    # 调用虚竹read方法
    wx.read()

    # 调用童姥see_prople方法
    wx.see_people('WYZ')
    wx.see_people('李秋水')
    wx.see_people('丁春秋')

    # 调用童姥fight_zms方法
    wx.fight_zms(1001, 80)