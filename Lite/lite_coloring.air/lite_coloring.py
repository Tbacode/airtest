'''
 * @Descripttion : 
 * @Author       : Tommy
 * @Date         : 2021-09-01 16:53:11
 * @LastEditors  : Tommy
 * @LastEditTime : 2021-09-07 17:53:08
'''
# -*- encoding=utf8 -*-
__author__ = "talefun"

from airtest.core.api import *
import sys
sys.path.append(r"C:\Users\talefun\Documents\airtest\Lite")
from img_RGB2location_lite import RGB2LocationLite
from BaseInit import baseInit

baseObject = baseInit()
dev = baseObject.init(flag=2)
sleep(10)
baseObject.is_enter_home(2)

# 进入图片
touch((280, 840))
sleep(10)
while True:
    if exists(Template(r"tpl1629345184802.png", record_pos=(-0.4, -0.802), resolution=(1080, 1920))):
        break
    sleep(2)

    
    
rgbLoc = RGB2LocationLite()
rgbLoc.run_main()

loc_list = baseObject.find_element_by_symbol(Template(r"tpl1629351309582.png", record_pos=(0.0, 0.638), resolution=(1080, 1920)), Template(r"tpl1629351322633.png", record_pos=(-0.232, 0.356), resolution=(1080, 1920)), Template(r"tpl1629351337019.png", record_pos=(-0.002, 0.357), resolution=(1080, 1920)), Template(r"tpl1629351348992.png", record_pos=(0.231, 0.356), resolution=(1080, 1920)))

# 点击收藏
if loc_list[0] is not None:
    touch(loc_list[0])
    sleep(2)
    baseObject.assert_exists_element(Template(r"tpl1629351451577.png", record_pos=(-0.232, 0.355), resolution=(1080, 1920)), "判定收藏成功")

# 点击保存
if loc_list[1] is not None:
    touch(loc_list[1])
    sleep(1)
    touch(Template(r"tpl1629353464696.png", record_pos=(0.127, -0.051), resolution=(1080, 1920)))
    sleep(1)

    # 获取权限弹窗
    touch(Template(r"tpl1629353526157.png", record_pos=(0.174, 0.096), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1629353546031.png", record_pos=(0.0, 0.038), resolution=(1080, 1920))) 

# 点击分享
if loc_list[2] is not None:
    touch(loc_list[2])
    sleep(1)
    touch(Template(r"tpl1629353464696.png", record_pos=(0.127, -0.051), resolution=(1080, 1920)))
    sleep(1)
    baseObject.assert_exists_element(Template(r"tpl1629353665446.png", record_pos=(0.003, -0.187), resolution=(1080, 1920)), "分享弹窗弹出")
    keyevent("KEYCODE_BACK")

# 点击继续回到主界面
touch(Template(r"tpl1629346420050.png", record_pos=(-0.001, 0.638), resolution=(1080, 1920)))


# 强制等待，写入数据，否则二次启动会再次弹出隐私弹窗
baseObject.exit_game(b_timeout=2)

# dev.stop_app("coloring.color.number.happy.paint.art.drawing.puzzle")


