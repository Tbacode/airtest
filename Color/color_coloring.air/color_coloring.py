# -*- encoding=utf8 -*-
__author__ = "talefun"

from airtest.core.api import *
import sys
sys.path.append(r"C:\Users\talefun\Documents\airtest\Color")
from img_RGB2location import RGB2Location
from BaseInit import baseInit

baseObject = baseInit()
dev = baseObject.init(flag=2)
baseObject.is_enter_home(2)

# 进入图片
touch((280, 840))
while True:
    if exists(Template(r"tpl1628584509786.png", record_pos=(0.143, -0.789), resolution=(1080, 1920))):
        break
    sleep(2)
    
    
# 商品购买
touch(Template(r"tpl1628584509786.png", record_pos=(0.143, -0.789), resolution=(1080, 1920)))
sleep(2)
swipe((527, 1563), (538, 65))
sleep(2)
touch((777, 666))
touch(Template(r"tpl1628756429439.png", record_pos=(0.0, 0.694), resolution=(1080, 1920)))
sleep(2)
calm_bt = wait(Template(r"tpl1628756452348.png", record_pos=(0.003, 0.236), resolution=(1080, 1920)))
sleep(2)
touch(calm_bt)
sleep(2)
print("填图初始化")
# import sys
# sys.path.append(r"C:\Users\xt875\Documents\airtest\Color_airtest.air")
    
# from img_RGB2location import RGB2Location
# rgbLoc = RGB2Location()

    
rgbLoc = RGB2Location()
rgbLoc.touch_init()
rgbLoc.run_main()

loc_list = baseObject.find_element_by_symbol(Template(r"tpl1631008163498.png", record_pos=(-0.002, 0.631), resolution=(1080, 1920)), Template(r"tpl1629097462808.png", record_pos=(-0.002, 0.395), resolution=(1080, 1920)), Template(r"tpl1629097675190.png", record_pos=(-0.235, 0.394), resolution=(1080, 1920)), Template(r"tpl1631008647087.png", record_pos=(0.234, 0.394), resolution=(1080, 1920)))

# 点击保存
if loc_list[0] is not None:
    touch(loc_list[0])
    sleep(2)
    touch(Template(r"tpl1629097548318.png", record_pos=(0.119, 0.017), resolution=(1080, 1920)))
    sleep(1)
    # 权限弹窗
    if exists(Template(r"tpl1629097618079.png", record_pos=(0.0, -0.164), resolution=(1080, 1920))):
        touch(Template(r"tpl1631008444934.png", record_pos=(-0.164, 0.092), resolution=(1080, 1920)))
        sleep(2)
        touch(Template(r"tpl1629097648055.png", record_pos=(-0.002, 0.036), resolution=(1080, 1920)))
        sleep(1)
        
# 点击喜欢
if loc_list[1] is not None:
    touch(loc_list[1])
    sleep(2)
    baseObject.assert_exists_element(Template(r"tpl1629097714571.png", record_pos=(-0.234, 0.392), resolution=(1080, 1920)), "判定收藏成功")
    
# 点击分享
if loc_list[2] is not None:
    touch(loc_list[2])
    sleep(1)
    touch(Template(r"tpl1629097548318.png", record_pos=(0.119, 0.017), resolution=(1080, 1920)))
    sleep(1)
    baseObject.assert_exists_element(Template(r"tpl1631008727167.png", record_pos=(0.0, -0.189), resolution=(1080, 1920)), "判定分享弹窗成功")
    keyevent("KEYCODE_BACK")

# 返回主界面
touch(Template(r"tpl1631008163498.png", record_pos=(-0.002, 0.631), resolution=(1080, 1920)))




# 成就大师
touch(Template(r"tpl1628756452348.png", record_pos=(0.003, 0.236), resolution=(1080, 1920)))
sleep(1)
# 点击消除新手引导
touch((943, 1851))

# 强制等待，写入数据，否则二次启动会再次弹出隐私弹窗
baseObject.exit_game(b_timeout=2)
