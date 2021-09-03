# -*- encoding=utf8 -*-
__author__ = "talefun"

from airtest.core.api import *

import sys
sys.path.append(r"C:\Users\talefun\Documents\airtest\Color")

from BaseInit import baseInit

baseObject = baseInit()
dev = baseObject.init(flag=2)

baseObject.is_enter_home(2)


# 进入mypainting
touch(Template(r"tpl1628654205391.png", record_pos=(0.378, 0.822), resolution=(1080, 1920)))
sleep(2)
touch(Template(r"tpl1628654222593.png", record_pos=(-0.43, -0.82), resolution=(1080, 1920)))
sleep(2)


ele_list = baseObject.find_element_by_symbol(Template(r"tpl1630655159788.png", record_pos=(-0.001, -0.821), resolution=(1080, 1920)), Template(r"tpl1630655216756.png", record_pos=(-0.378, -0.481), resolution=(1080, 1920)), Template(r"tpl1630655309284.png", record_pos=(-0.371, -0.279), resolution=(1080, 1920)), Template(r"tpl1630655328199.png", record_pos=(-0.371, -0.122), resolution=(1080, 1920)))
print("ele_list--------->",ele_list )

# 点击问卷调查
if ele_list[0] is not None:
    touch(ele_list[0])
    baseObject.assert_exists_element(Template(r"tpl1630655540137.png", record_pos=(-0.015, -0.814), resolution=(1080, 1920)), "有奖调查打开成功", b_time=3, a_time=3)
    touch(Template(r"tpl1630657665125.png", record_pos=(-0.411, -0.806), resolution=(1080, 1920)))
    sleep(1)
    
# 点击填色阴影切换
if ele_list[1] is not None:
    touch(ele_list[1])
    sleep(2)
    touch(Template(r"tpl1630655665118.png", record_pos=(0.294, -0.57), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1630657665125.png", record_pos=(-0.411, -0.806), resolution=(1080, 1920)))

    
# 点击隐藏图片
if ele_list[2] is not None:
    touch(ele_list[2])
    sleep(1)
    
    
# 滑动到底
swipe((500, 1344), (504, 153))
sleep(3)


# 获取底部setting元素
ele_list = baseObject.find_element_by_symbol(Template(r"tpl1630655159788.png", record_pos=(-0.001, -0.821), resolution=(1080, 1920)), Template(r"tpl1630655889568.png", record_pos=(-0.37, 0.143), resolution=(1080, 1920)), Template(r"tpl1630655900053.png", record_pos=(-0.37, 0.3), resolution=(1080, 1920)), Template(r"tpl1630655915842.png", record_pos=(-0.371, 0.456), resolution=(1080, 1920)), Template(r"tpl1630655931416.png", record_pos=(-0.371, 0.612), resolution=(1080, 1920)))


# 点击FAQ
if ele_list[0] is not None:
    touch(ele_list[0])
    sleep(1)
    baseObject.assert_exists_element(Template(r"tpl1628664646850.png", record_pos=(-0.002, -0.706), resolution=(1080, 1920)), "FAQ进入成功", b_time=10)
    keyevent("KEYCODE_BACK")
    sleep(1)
    
# 点击邮件联系
if ele_list[1] is not None:
    touch(ele_list[1])
    sleep(2)
    touch(Template(r"tpl1630656287049.png", record_pos=(-0.375, 0.623), resolution=(1080, 1920)))
    sleep(3)
    if dev.get_top_activity_name() == "com.google.android.gm/.ComposeActivityGmailExternal":
        keyevent("KEYCODE_BACK")
    sleep(1)
    keyevent("KEYCODE_BACK")
    sleep(2)
    
# 点击服务条款链接
if ele_list[3] is not None:
    touch(ele_list[3])
    sleep(10)
    act_name = dev.get_top_activity_name()
    baseObject.assert_equal_element(act_name, "com.pixel.art.coloring.by.number/talefun.cd.sdk.webview.MyWebViewActivity", "服务条款链接是否正常跳出")
    baseObject.assert_exists_element(Template(r"tpl1628653574859.png", record_pos=(-0.314, -0.596), resolution=(1080, 1920)), "判断是否正常显示服务条款页面")
    keyevent("KEYCODE_BACK")
    sleep(1)
    
# 点击隐私协议链接
if ele_list[2] is not None:
    touch(ele_list[2])
    sleep(10)
    act_name = dev.get_top_activity_name()
    baseObject.assert_equal_element(act_name, "com.pixel.art.coloring.by.number/talefun.cd.sdk.webview.MyWebViewActivity", "隐私协议链接是否正常跳出")
    baseObject.assert_exists_element(Template(r"tpl1628653574859.png", record_pos=(-0.314, -0.596), resolution=(1080, 1920)), "判断是否正常显示服务条款页面")
    keyevent("KEYCODE_BACK")
    sleep(1)

dev.stop_app("com.pixel.art.coloring.by.number")