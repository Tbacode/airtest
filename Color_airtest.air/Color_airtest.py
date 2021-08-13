'''
Author: your name
Date: 2021-08-04 15:25:24
LastEditTime: 2021-08-10 11:56:51
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Color_airtest.air\Color_airtest.py
'''
# -*- encoding=utf8 -*-
__author__ = "xt875"

from airtest.core.api import *
from airtest.core.android.android import Android

auto_setup(__file__)

def init(packagename):
    dev = Android()
    if not dev.is_locked():
        dev.unlock()
    dev.clear_app(packagename)
    dev.start_app(packagename)
    return dev

def is_enter_home():
    if exists(Template(r"tpl1628762015501.png", record_pos=(-0.005, -0.243), resolution=(1080, 1920))):
        agree_bt = wait(Template(r"tpl1628062510559.png", record_pos=(0.002, 0.304), resolution=(1080, 1920)))
        terms_link = wait(Template(r"tpl1628062685346.png", record_pos=(-0.169, 0.099), resolution=(1080, 1920)))
        print(terms_link)
        privacy_link = wait(Template(r"tpl1628062704363.png", record_pos=(0.022, 0.095), resolution=(1080, 1920)))
        print(privacy_link)
        return agree_bt, terms_link, privacy_link
    else:
        is_enter_home()
        
packagename = 'com.pixel.art.coloring.by.number'
launch_activity = 'com.unity3d.player.UnityPlayerActivity'

# dev = init(packagename)
# sleep(10)
# agree_bt, terms_link, privacy_link = is_enter_home()

# touch(terms_link)
# sleep(10)
# flag = False
# act_name = dev.get_top_activity_name()
# try:
#     assert_equal(act_name, "com.pixel.art.coloring.by.number/talefun.cd.sdk.webview.MyWebViewActivity", "服务条款链接是否正常跳出")
# except:
#     print("跳出失败")
# if exists(Template(r"tpl1628653574859.png", record_pos=(-0.314, -0.596), resolution=(1080, 1920))):
#     flag = True
# try:
#     assert_equal(flag, True, "判断是否正常显示服务条款页面")
# except:
#     print("显示失败")
# keyevent('KEYCODE_BACK')
# sleep(1)
# touch(privacy_link)
# sleep(10)
# act_name = dev.get_top_activity_name()
# flag = False
# try:
#     assert_equal(act_name, "com.pixel.art.coloring.by.number/talefun.cd.sdk.webview.MyWebViewActivity", "隐私协议链接是否正常跳出")
# except:
#     print("跳出失败")
# if exists(Template(r"tpl1628653574859.png", record_pos=(-0.314, -0.596), resolution=(1080, 1920))):
#     flag = True
# try:
#     assert_equal(flag, True, "判断是否正常显示服务条款页面")
# except:
#     print("显示失败")
# keyevent('KEYCODE_BACK')
# sleep(3)
# touch(agree_bt)
# sleep(1)

# # 进入mypainting
# touch(Template(r"tpl1628654205391.png", record_pos=(0.378, 0.822), resolution=(1080, 1920)))
# sleep(2)
# touch(Template(r"tpl1628654222593.png", record_pos=(-0.43, -0.82), resolution=(1080, 1920)))
# sleep(2)
# touch(Template(r"tpl1628666829596.png", record_pos=(-0.37, -0.632), resolution=(1080, 1920)))
# sleep(1)
# try:
#     assert_exists(Template(r"tpl1628666871971.png", record_pos=(-0.018, -0.809), resolution=(1080, 1920)), "有奖调查打开成功")
#     touch(Template(r"tpl1628654344533.png", record_pos=(-0.407, -0.793), resolution=(1080, 1920)))
#     sleep(1)
# except Exception as e:
#     print("打开失败")
#     raise e
# touch(Template(r"tpl1628654268937.png", record_pos=(-0.37, -0.313), resolution=(1080, 1920)))
# touch(Template(r"tpl1628654287761.png", record_pos=(-0.372, 0.473), resolution=(1080, 1920)))
# sleep(1)
# touch(Template(r"tpl1628654314042.png", record_pos=(0.294, -0.564), resolution=(1080, 1920)))
# touch(Template(r"tpl1628654344533.png", record_pos=(-0.407, -0.793), resolution=(1080, 1920)))
# sleep(1)
# swipe((500, 1344), (504, 153))
# sleep(3)
# touch(Template(r"tpl1628664592422.png", record_pos=(-0.373, -0.165), resolution=(1080, 1920)))
# sleep(10)
# try:
#     assert_exists(Template(r"tpl1628664646850.png", record_pos=(-0.002, -0.706), resolution=(1080, 1920)), "FAQ打开成功")
# except:
#     print("打开失败")
# keyevent("KEYCODE_BACK")
# sleep(1)
# touch(Template(r"tpl1628664735847.png", record_pos=(-0.37, 0.146), resolution=(1080, 1920)))
# if exists(Template(r"tpl1628664777138.png", record_pos=(-0.378, 0.621), resolution=(1080, 1920))):
#     touch(Template(r"tpl1628664777138.png", record_pos=(-0.378, 0.621), resolution=(1080, 1920)))
#     sleep(3)
#     act_name = dev.get_top_activity_name()
#     print(act_name)
#     try:
#         assert_equal(act_name, "com.google.android.gm/.ComposeActivityGmailExternal", "邮箱弹出")
#         keyevent("KEYCODE_BACK")
#         sleep(0.5)
#         keyevent("KEYCODE_BACK")
#     except Exception as e:
#         print("邮箱弹出失败")
#         raise e
        
# touch(Template(r"tpl1628665851814.png", record_pos=(-0.371, 0.463), resolution=(1080, 1920)))
# sleep(10)
# flag = False
# act_name = dev.get_top_activity_name()
# try:
#     assert_equal(act_name, "com.pixel.art.coloring.by.number/talefun.cd.sdk.webview.MyWebViewActivity", "服务条款链接是否正常跳出")
# except:
#     print("跳出失败")
# if exists(Template(r"tpl1628653574859.png", record_pos=(-0.314, -0.596), resolution=(1080, 1920))):
#     flag = True
# try:
#     assert_equal(flag, True, "判断是否正常显示服务条款页面")
# except:
#     print("显示失败")
# keyevent('KEYCODE_BACK')
# sleep(1)
# touch(Template(r"tpl1628665908967.png", record_pos=(-0.372, 0.621), resolution=(1080, 1920)))
# sleep(10)
# act_name = dev.get_top_activity_name()
# flag = False
# try:
#     assert_equal(act_name, "com.pixel.art.coloring.by.number/talefun.cd.sdk.webview.MyWebViewActivity", "隐私协议链接是否正常跳出")
# except:
#     print("跳出失败")
# if exists(Template(r"tpl1628653574859.png", record_pos=(-0.314, -0.596), resolution=(1080, 1920))):
#     flag = True
# try:
#     assert_equal(flag, True, "判断是否正常显示服务条款页面")
# except:
#     print("显示失败")
# keyevent('KEYCODE_BACK')
# sleep(1)
# touch(Template(r"tpl1628654344533.png", record_pos=(-0.407, -0.793), resolution=(1080, 1920)))
# sleep(1)
# touch(Template(r"tpl1628668000544.png", record_pos=(-0.38, 0.82), resolution=(1080, 1920)))
# sleep(2)

# # 进入图片
# touch((280, 840))
# try:
#     wait(Template(r"tpl1628584509786.png", record_pos=(0.143, -0.789), resolution=(1080, 1920)), timeout=60)
# except Exception as e:
#     print("进图失败")
#     raise e
# else:
#     import sys
#     sys.path.append(r"C:\Users\xt875\Documents\airtest\Color_airtest.air")
#     from img_RGB2location import RGB2Location
#     rgbLoc = RGB2Location()
# # 商品购买
# touch(Template(r"tpl1628584509786.png", record_pos=(0.143, -0.789), resolution=(1080, 1920)))
# sleep(2)
# swipe((527, 1563), (538, 65))
# sleep(2)
# touch((777, 666))
# touch(Template(r"tpl1628756429439.png", record_pos=(0.0, 0.694), resolution=(1080, 1920)))
# sleep(2)
# calm_bt = wait(Template(r"tpl1628756452348.png", record_pos=(0.003, 0.236), resolution=(1080, 1920)))
# sleep(2)
# touch(calm_bt)
# sleep(2)
print("填图初始化")
import sys
sys.path.append(r"C:\Users\xt875\Documents\airtest\Color_airtest.air")
    
from img_RGB2location import RGB2Location
rgbLoc = RGB2Location()
rgbLoc.touch_init()       
    
rgbLoc.run_main()

# 成就大师
touch(Template(r"tpl1628756452348.png", record_pos=(0.003, 0.236), resolution=(1080, 1920)))
sleep(1)
# 点击消除新手引导
touch((943, 1851))



