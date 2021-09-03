# -*- encoding=utf8 -*-
__author__ = "talefun"

from airtest.core.api import *
import sys

sys.path.append(r"C:\Users\talefun\Documents\airtest\Lite")
from BaseInit import baseInit

baseObject = baseInit()
dev = baseObject.init(flag=2)

baseObject.is_enter_home(2)
sleep(2)



# 进入我的界面
touch(Template(r"tpl1629274844658.png", record_pos=(0.354, 0.814), resolution=(1080, 1920)))
sleep(1)

# 进入设置界面
touch(Template(r"tpl1629274873255.png", record_pos=(0.422, -0.794), resolution=(1080, 1920)))
sleep(2)
ele_list = baseObject.find_element_by_symbol(Template(r"tpl1629276407176.png", record_pos=(0.0, -0.794), resolution=(1080, 1920)), Template(r"tpl1629276435332.png", record_pos=(-0.39, -0.615), resolution=(1080, 1920)), Template(r"tpl1629276459770.png", record_pos=(-0.391, -0.116), resolution=(1080, 1920)), Template(r"tpl1629276484996.png", record_pos=(-0.39, 0.345), resolution=(1080, 1920)), Template(r"tpl1629279819991.png", record_pos=(-0.39, 0.719), resolution=(1080, 1920)))
# 点击问卷调查
if ele_list[0] is not None:
    touch(ele_list[0])
    baseObject.assert_exists_element(Template(r"tpl1629277476305.png", record_pos=(-0.018, -0.803), resolution=(1080, 1920)), "有奖调查打开成功", b_time=3, a_time=3)
    keyevent("KEYCODE_BACK")
    sleep(1)
# 点击隐藏已完成图片
if ele_list[1] is not None:
    touch(ele_list[1])
    sleep(1)
# 点击填色阴影切换
if ele_list[2] is not None:
    touch(ele_list[2])
    sleep(2)
    touch(Template(r"tpl1629277758415.png", record_pos=(0.292, -0.519), resolution=(1080, 1920)))
    sleep(1)
    keyevent("KEYCODE_BACK")
    
# 点击商店按钮
if ele_list[3] is not None:
    touch(ele_list[3])
    sleep(2)
    swipe((527, 1563), (538, 65))
    sleep(3)
    touch((794, 706))
    sleep(3)
    touch(Template(r"tpl1629280156765.png", record_pos=(0.0, 0.694), resolution=(1080, 1920)))
    sleep(3)
    touch(Template(r"tpl1629280184723.png", record_pos=(0.002, 0.229), resolution=(1080, 1920)))
    sleep(2)
    


touch(Template(r"tpl1629274873255.png", record_pos=(0.422, -0.794), resolution=(1080, 1920)))
sleep(2)

if ele_list[3] is not None:
    touch(ele_list[3])
    sleep(2)
    swipe((527, 1563), (538, 65))
    sleep(3)
    touch((794, 706))
    sleep(3)
    touch(Template(r"tpl1629280156765.png", record_pos=(0.0, 0.694), resolution=(1080, 1920)))
    sleep(3)
    touch(Template(r"tpl1629280184723.png", record_pos=(0.002, 0.229), resolution=(1080, 1920)))
    sleep(2)
    

touch(Template(r"tpl1629274873255.png", record_pos=(0.422, -0.794), resolution=(1080, 1920)))
sleep(2)


# 滑动列表
swipe((500, 1344), (504, 153))
sleep(2)

ele_list = baseObject.find_element_by_symbol(Template(r"tpl1629276407176.png", record_pos=(0.0, -0.794), resolution=(1080, 1920)), Template(r"tpl1629277958167.png", record_pos=(-0.391, -0.067), resolution=(1080, 1920)), Template(r"tpl1629277977418.png", record_pos=(-0.389, 0.086), resolution=(1080, 1920)), Template(r"tpl1629277991740.png", record_pos=(-0.389, 0.389), resolution=(1080, 1920)), Template(r"tpl1629278003613.png", record_pos=(-0.393, 0.546), resolution=(1080, 1920)))
# 点击FAQ
if ele_list[0] is not None:
    touch(ele_list[0])
    baseObject.assert_exists_element(Template(r"tpl1629278428239.png", record_pos=(0.005, -0.706), resolution=(1080, 1920)), "FAQ进入成功", b_time=10)
    keyevent("KEYCODE_BACK")
    sleep(1)
    
# 点击联系我们
if ele_list[1] is not None:
    touch(ele_list[1])
    sleep(2)
    touch(Template(r"tpl1629278671599.png", threshold=0.8500000000000001, record_pos=(-0.377, 0.622), resolution=(1080, 1920)))
    sleep(3)
    keyevent("KEYCODE_BACK")
    sleep(1)
    keyevent("KEYCODE_BACK")
    
# 点击隐私协议
if ele_list[2] is not None:
    touch(ele_list[2])
    sleep(10)
    act_name = dev.get_top_activity_name()
    baseObject.assert_equal_element(act_name, "coloring.color.number.happy.paint.art.drawing.puzzle/talefun.cd.sdk.webview.MyWebViewActivity", "隐私协议链接是否正常跳出")
    baseObject.assert_exists_element(Template(r"tpl1629273292532.png", record_pos=(-0.311, -0.596), resolution=(1080, 1920)), "判断是否正常显示隐私协议页面")
    keyevent("KEYCODE_BACK")
    sleep(1)

# 点击使用条款
if ele_list[3] is not None:
    touch(ele_list[3])
    sleep(10)
    act_name = dev.get_top_activity_name()
    baseObject.assert_equal_element(act_name, "coloring.color.number.happy.paint.art.drawing.puzzle/talefun.cd.sdk.webview.MyWebViewActivity", "隐私服务条款是否正常跳出")
    baseObject.assert_exists_element(Template(r"tpl1629273292532.png", record_pos=(-0.311, -0.596), resolution=(1080, 1920)), "判断是否正常显示服务条款页面")
    keyevent("KEYCODE_BACK")
    sleep(1)

keyevent("KEYCODE_BACK")
sleep(1)
touch(Template(r"tpl1629279032067.png", record_pos=(-0.356, 0.813), resolution=(1080, 1920)))
sleep(1)

dev.stop_app("coloring.color.number.happy.paint.art.drawing.puzzle")
