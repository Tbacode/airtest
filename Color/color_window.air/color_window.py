# -*- encoding=utf8 -*-
__author__ = "talefun"

from airtest.core.api import *
from airtest.core.android.android import Android
import sys
sys.path.append(r"C:\Users\talefun\Documents\airtest\Color")

from BaseInit import baseInit


IS_DAILY_REWARD_CLAIM = False

# 设置调整
def start_init(timeout=10):
    sleep(timeout)
    # 判定进入成功
    if exists(Template(r"tpl1632379053300.png", record_pos=(0.002, -0.294), resolution=(1080, 1920))):
        sleep(1)
        touch(Template(r"tpl1632379073159.png", record_pos=(0.001, 0.334), resolution=(1080, 1920)))
        sleep(1)
        touch(Template(r"tpl1632379136191.png", record_pos=(0.377, 0.807), resolution=(1080, 1920)))
        sleep(1)
        touch(Template(r"tpl1632379150281.png", record_pos=(-0.428, -0.82), resolution=(1080, 1920)))
        sleep(1)
        touch(Template(r"tpl1632379204596.png", record_pos=(-0.076, -0.12), resolution=(1080, 1920)))
        sleep(1)
        keyevent("KEYCODE_BACK")
        sleep(1)
        touch((104, 796))
        touch((104, 796))
        sleep(1)
        touch(Template(r"tpl1632379306785.png", record_pos=(-0.412, -0.445), resolution=(1080, 1920)))
        sleep(1)
        touch(Template(r"tpl1632379323218.png", record_pos=(-0.156, -0.465), resolution=(1080, 1920)))
        touch((1038, 40))
        sleep(1)
        touch(Template(r"tpl1632379719956.png", record_pos=(-0.378, 0.803), resolution=(1080, 1920)))

    else:
        start_init(3)

# 点击paintall按钮
def click_paintAll():
    if wait(Template(r"tpl1632379909482.png", record_pos=(0.281, -0.797), resolution=(1080, 1920)), 600):
        touch((924, 319))


# 进入首图
def enter_pic():
    if exists(Template(r"tpl1632379852371.png", record_pos=(-0.39, -0.386), resolution=(1080, 1920))):
        touch((266, 837))


# 普通图是否完成
def is_normalPic_finish(timeout=10):
    sleep(timeout)
    try:
        wait(Template(r"tpl1632380568529.png", record_pos=(0.001, 0.634), resolution=(1080, 1920)))
    except:
        is_animatedPic_finish()
    else:
        daily_task_claim()
        sleep(3)
        touch(Template(r"tpl1632380568529.png", record_pos=(0.001, 0.634), resolution=(1080, 1920)))

# 动图是否完成
def is_animatedPic_finish():
    if exists(Template(r"tpl1632380500506.png", record_pos=(0.0, 0.424), resolution=(1080, 1920))):
        touch(Template(r"tpl1632380500506.png", record_pos=(0.0, 0.424), resolution=(1080, 1920)))
        sleep(3)
        daily_task_claim()
        touch(Template(r"tpl1632380568529.png", record_pos=(0.001, 0.634), resolution=(1080, 1920)))

    else:
        is_normalPic_finish(3)


# APP进入后台
def set_app_backup():
    home()

# APP进入前台
def set_app_wakeup():
    start_app("com.pixel.art.coloring.by.number")

# 每日任务领取判定
def daily_task_claim():
    global IS_DAILY_REWARD_CLAIM
    # 领取每日任务奖励
    if not IS_DAILY_REWARD_CLAIM:
        sleep(5)
        if exists(Template(r"tpl1632383918270.png", record_pos=(-0.004, -0.672), resolution=(1080, 1920))):
            touch(Template(r"tpl1632380680715.png", record_pos=(0.002, 0.444), resolution=(1080, 1920)))
            sleep(1)
            IS_DAILY_REWARD_CLAIM = True

# fb登录弹窗
def bf_window_appear():
    try:
        assert_exists(Template(r"tpl1632638890972.png", record_pos=(0.002, -0.438), resolution=(1080, 1920)), "fb弹窗弹出正常")
    except:
        print("fb弹窗弹出异常")
    else:
        touch(Template(r"tpl1632638990695.png", record_pos=(-0.003, 0.423), resolution=(1080, 1920)))


        


# 评论引导弹窗
def comment_window_appear():
    dev = Android()
    if exists(Template(r"tpl1632466215524.png", record_pos=(0.0, -0.117), resolution=(1080, 1920))):
        touch((771, 1016))
        sleep(1)
        if exists(Template(r"tpl1632467055213.png", record_pos=(0.003, 0.048), resolution=(1080, 1920))):
            touch(Template(r"tpl1632467072074.png", record_pos=(0.0, 0.19), resolution=(1080, 1920)))
            # 等待商店跳转
            sleep(10)
            try:
                assert_equal("com.android.vending/com.google.android.finsky.activities.MainActivity", str(dev.get_top_activity_name()), "5星好评跳转正常")
            except:
                print("跳转商店异常")
            keyevent("KEYCODE_BACK")
        else:
            touch(Template(r"tpl1632467154432.png", record_pos=(0.415, -0.299), resolution=(1080, 1920)))

# 插屏广告判定
def is_interAD_show():
    dev = Android()
    if "com.unity3d.player.UnityPlayerActivity" not in str(dev.get_top_activity_name()):
        return True
    return False

# 主入口函数
def main(finish_pic_num):
    
    enter_pic()
    sleep(3)
    if is_interAD_show():
        set_app_backup()
        sleep(1.0)
        set_app_wakeup()
    click_paintAll()
    is_normalPic_finish()
    sleep(3)
    if is_interAD_show():
        set_app_backup()
        sleep(1.0)
        set_app_wakeup()
    # 首张图完成后，点击领取成就奖励
    if finish_pic_num == 1:
        if exists(Template(r"tpl1632380716429.png", record_pos=(-0.004, -0.481), resolution=(1080, 1920))):

            touch(Template(r"tpl1632380680715.png", record_pos=(0.002, 0.444), resolution=(1080, 1920)))
            sleep(1)
            # 点击取消成就提示
            touch((957, 1842))
    # 引导评论弹窗
    if finish_pic_num == 12:
        comment_window_appear()
    # 17张图片完成后，fb引导弹窗判定
    if finish_pic_num == 17:
        bf_window_appear()


    
# 启动游戏
baseObject = baseInit()
baseObject.init()
start_init()   
for i in range(1, 25):
    main(i)
