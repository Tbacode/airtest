# -*- encoding=utf8 -*-
__author__ = "Tommy"

from airtest.core.api import *

import sys
sys.path.append(r"C:\Users\talefun\Documents\airtest\Color")

from BaseInit import baseInit

baseObject = baseInit()
dev = baseObject.init()


# 获取隐私弹窗元素
agree_bt, terms_link, privacy_link = baseObject.is_enter_home()

# 点击服务条款链接
if terms_link is not None:
    touch(terms_link)
    sleep(10)
    act_name = dev.get_top_activity_name()
    baseObject.assert_equal_element(act_name, "com.pixel.art.coloring.by.number/talefun.cd.sdk.webview.MyWebViewActivity", "服务条款链接是否正常跳出")
    baseObject.assert_exists_element(Template(r"tpl1628653574859.png", record_pos=(-0.314, -0.596), resolution=(1080, 1920)), "判断是否正常希纳是服务条款页面")
    keyevent("KEYCODE_BACK")
    sleep(1)
    
# 点击隐私协议链接
if privacy_link is not None:
    touch(privacy_link)
    sleep(10)
    act_name = dev.get_top_activity_name()
    baseObject.assert_equal_element(act_name, "com.pixel.art.coloring.by.number/talefun.cd.sdk.webview.MyWebViewActivity", "隐私协议链接是否正常跳出")
    baseObject.assert_exists_element(Template(r"tpl1628653574859.png", record_pos=(-0.314, -0.596), resolution=(1080, 1920)), "判断是否正常显示服务条款页面")
    keyevent("KEYCODE_BACK")
    sleep(1)
    
# 点击继续
touch(agree_bt)

sleep(2)


baseObject.exit_game(b_timeout=2)
# dev.stop_app("com.pixel.art.coloring.by.number")