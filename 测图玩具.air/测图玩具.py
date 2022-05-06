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
    if wait(Template(r"tpl1637056383586.png", record_pos=(-0.376, -0.367), resolution=(1080, 1920)), 600):
#         touch((350, 1316))

        touch((280, 850))
#         touch((174, 614))
          
    
# 点击paint All
def click_paintAll():
    if wait(Template(r"tpl1639557491122.png", record_pos=(0.129, -0.783), resolution=(1080, 1920)), 300):

        touch(Template(r"tpl1640588790828.png", record_pos=(0.37, -0.676), resolution=(1080, 2340)))

    
# 判断是否App在前台
def is_APP_resumeActivity(launch_activity):
    result = AdbOperation()
    tag = result.isRunningAppActivity()
    print("当前ACTIVITY：" + tag)
    if launch_activity in tag:
        return True
    else:
        return False

# 判断是否普通图完成
def is_normalPic_finish():
    sleep(5)
    try:
        wait(Template(r"tpl1639557534134.png", record_pos=(0.001, 0.436), resolution=(1080, 1920)))
    except:
        pass
    else:
        try:
            touch(Template(r"tpl1639557534134.png", record_pos=(0.001, 0.436), resolution=(1080, 1920)))
        except:
            pass
    try:
        wait(Template(r"tpl1639557559823.png", record_pos=(-0.004, 0.638), resolution=(1080, 1920)))

    except:
        click_animatedPic_continue()
    else:
#         sleep(3)
        touch(Template(r"tpl1639557559823.png", record_pos=(-0.004, 0.638), resolution=(1080, 1920)))
# 动图完成情况继续
def click_animatedPic_continue():
    try:
        next_bt = wait(Template(r"tpl1639557534134.png", record_pos=(0.001, 0.436), resolution=(1080, 1920)))
    except:
        is_normalPic_finish()
    else:
        click(next_bt)
        sleep(3)
        tag = wait(Template(r"tpl1639557559823.png", record_pos=(-0.004, 0.638), resolution=(1080, 1920)))
        sleep(3)
        if tag:
            touch(tag)
            sleep(2)
        
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
launch_activity = "com.unity3d.player.UnityPlayerActivity"
index = 8 # 每日终审图数量
while index != 0:
    main(packagename, launch_activity)
    index -= 1
    print(index)
# print(is_APP_resumeActivity(launch_activity))


