'''
Author: your name
Date: 2021-07-05 16:53:38
LastEditTime: 2021-07-08 10:48:50
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \air脚本\BBB_airtest.air\BBB_airtest.py
'''
# -*- encoding=utf8 -*-
__author__ = "xt875"


from airtest.core.api import *
from airtest.core.android.android import Android
from airtest.report.report import simple_report
# import sys
# sys.path.append(r'C:\Users\xt875\Desktop\air脚本\BBB_airtest.air')


using('BBB_airtest.air')



auto_setup(__file__)

# packagename = "com.brick.breaker.ball.shooting.blast"


def init(packagename):
    dev = Android()
    if not dev.is_locked():
        dev.unlock()
    dev.clear_app(packagename)
    dev.start_app(packagename)
    
    

    # connect_device("HT7941A04009")
home_bt = (554, 1800)
packagename = "com.brick.breaker.ball.shooting.blast"
init(packagename)
sleep(5)
from newuser_skip import user_skip
user_skip.run_skip()
sleep(2)
# 关闭弹窗
touch(wait(Template(r"close.png", record_pos=(0.361, -0.617), resolution=(1080, 1920))))
sleep(3)

# 进入商店
touch((99, 1820))
from shop_page import shop
shop.run_shop()
# 其余按钮坐标相对home来定，需要切换回home
touch(home_bt)

from level_finish import levelfinish
levelfinish.run_level_main()

touch(wait(Template(r"tpl1626146563117.png", record_pos=(0.434, -0.619), resolution=(1080, 1920))))

sleep(2)
from settingpage import set_page
set_page.run_setpage()
sleep(3)


# # 进入商店
# touch((99, 1820))
# from shop_page import shop
# shop.run_shop()
# 其余按钮坐标相对home来定，需要切换回home
# touch(home_bt)
# if exists(Template(r"close.png", record_pos=(0.361, -0.617), resolution=(1080, 1920))):
#     touch(exists(Template(r"close.png", record_pos=(0.361, -0.617), resolution=(1080, 1920))))
# 进入球背包
touch((295, 1800))
# 等待滑动
sleep(1)
touch(wait(Template(r"tpl1626230764089.png", record_pos=(0.0, 0.394), resolution=(1080, 1920))))
# 进入挑战关
touch((990, 1800))
from survivial_page import survivial
survivial.run_survivial()
sleep(3)
touch(home_bt)

# from activity_page import act
# img_dict = act.run_activity()
# touch(img_dict["img_bt"])
# assert_exists(img_dict["assert_img"], "每日活动是否配对正常")
# simple_report(__file__)


