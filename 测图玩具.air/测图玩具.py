'''
 * @Descripttion : 
 * @Author       : Tommy
 * @Date         : 2020-11-26 19:30:36
 * @LastEditors  : Tommy
 * @LastEditTime : 2020-11-26 19:58:45
'''
# -*- encoding=utf8 -*-
__author__ = "xt875"

import sys
sys.path.append(r'C:\Users\xt875\Desktop\air脚本\测图玩具.air')
from airtest.core.api import *
using('测图玩具.air')
from AdbOperation import AdbOperation

# 点击进入首张图片
def inter_firstPic():
    if wait(Template(r"tpl1606727235889.png", record_pos=(-0.135, -0.509), resolution=(1440, 2880)), 600):

        touch((325, 1787))
    
# 点击paint All
def click_paintAll():
    if wait(Template(r"tpl1606727439559.png", record_pos=(0.138, -0.91), resolution=(1440, 2880)), 600):

        touch((1260, 430))
    
# 判断是否App在前台
def is_APP_resumeActivity(launch_activity):
    result = AdbOperation()
    tag = result.isRunningAppActivity()
    # print(tag)
    if launch_activity in tag:
        return True
    else:
        return False

# 判断是否普通图完成
def is_normalPic_finish():
    sleep(10)
    if wait(Template(r"tpl1606723301999.png", record_pos=(-0.003, 0.625), resolution=(1440, 2880))):
        touch(exists(Template(r"tpl1606723301999.png", record_pos=(-0.003, 0.625), resolution=(1440, 2880))))
    else:
        wait(Template(r"tpl1606723301999.png", record_pos=(-0.003, 0.625), resolution=(1440, 2880)),20,click_animatedPic_continue(), 0.5)
# 动图完成情况继续
def click_animatedPic_continue():
    try:
        next_bt = wait(Template(r"tpl1606723602379.png", record_pos=(-0.001, 0.423), resolution=(1440, 2880)))
    except:
        is_normalPic_finish()
    else:
        click(next_bt)
        tag = wait(Template(r"tpl1606723301999.png", record_pos=(-0.003, 0.625), resolution=(1440, 2880)), 600)
        if tag:
            touch(tag)
        
# APP进入后台后再次进入前台
def set_activity_backup():
    result = AdbOperation()
    result.set_app_backup()
    
# 唤醒app从后台到前台
def app_wakeup(packagename, launch_activity):
    result = AdbOperation()
    result.app_wakeup(packagename, launch_activity)

# main方法入口
def main(packagename, launch_activity):
    inter_firstPic()
    sleep(5)
    if not is_APP_resumeActivity(launch_activity):
        set_activity_backup()
        sleep(3.0)
        app_wakeup(packagename, launch_activity)
    click_paintAll()
    is_normalPic_finish()
    sleep(5)
    if not is_APP_resumeActivity(launch_activity):
        set_activity_backup()
        sleep(3.0)
        app_wakeup(packagename, launch_activity)
        # main(packagename, launch_activity)
    
    

packagename = "com.pixel.art.coloring.by.number"
launch_activity = ".UnityPlayerActivity"
index = 3 # 每日终审图数量
while index != 0:
    main(packagename, launch_activity)
    index -= 1
    print(index)
# print(is_APP_resumeActivity(launch_activity))

