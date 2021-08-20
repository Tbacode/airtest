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
    if exists(Template(r"tpl1629269284035.png", record_pos=(-0.001, -0.379), resolution=(1080, 1920))):
        agree_bt = wait_element(Template(r"tpl1629279181598.png", record_pos=(-0.004, 0.193), resolution=(1080, 1920)))
        terms_link = wait_element(Template(r"tpl1629279205859.png", record_pos=(-0.149, -0.012), resolution=(1080, 1920)))
        print(terms_link)
        privacy_link = wait_element(Template(r"tpl1629279228084.png", record_pos=(0.061, -0.013), resolution=(1080, 1920)))
        print(privacy_link)
        return agree_bt, terms_link, privacy_link
    else:
        is_enter_home()
        

def assert_exists_element(element, ass_msg, b_time=0, a_time=0):
    sleep(b_time)
    try:
        assert_exists(element, ass_msg)
    except AssertionError as f:
        raise f
    sleep(a_time)

def assert_equal_element(element, ass_element, ass_msg, b_time=0, a_time=0):
    sleep(b_time)
    try:
        assert_equal(element, ass_element, ass_msg)
    except AssertionError as f:
        raise f
    sleep(a_time)
    
def wait_element(element, timeout=20, b_time=0, a_time=0):
    sleep(b_time)
    try:
        location = wait(element, timeout=timeout)
    except TargetNotFoundError as t:
        print("找不到该元素")
        location = None
        raise t
    sleep(a_time)
    return location

def find_element_by_symbol(sym_ele, *args):
    local_list = []
    if exists(sym_ele):
        for item_ele in args:
            local = wait_element(item_ele)
            local_list.append(local)
    return local_list
        
# packagename = " coloring.color.number.happy.paint.art.drawing.puzzle"
# launch_activity = "com.unity3d.player.UnityPlayerActivity"

# # 进入游戏
# dev = init(packagename)
# sleep(10)
# # 获取隐私弹窗元素
# agree_bt, terms_link, privacy_link = is_enter_home()

# # 点击服务条款链接
# if terms_link is not None:
#     touch(terms_link)
#     sleep(10)
#     act_name = dev.get_top_activity_name()
#     assert_equal_element(act_name, "coloring.color.number.happy.paint.art.drawing.puzzle/talefun.cd.sdk.webview.MyWebViewActivity", "服务条款链接是否正常跳出")
#     assert_exists_element(Template(r"tpl1629273292532.png", record_pos=(-0.311, -0.596), resolution=(1080, 1920)), "判断是否正常显示服务条款页面")
#     keyevent("KEYCODE_BACK")
#     sleep(1)
    
# # 点击隐私协议链接
# if privacy_link is not None:
#     touch(privacy_link)
#     sleep(10)
#     act_name = dev.get_top_activity_name()
#     assert_equal_element(act_name, "coloring.color.number.happy.paint.art.drawing.puzzle/talefun.cd.sdk.webview.MyWebViewActivity", "隐私协议链接是否正常跳出")
#     assert_exists_element(Template(r"tpl1629273292532.png", record_pos=(-0.311, -0.596), resolution=(1080, 1920)), "判断是否正常显示隐私协议页面")
#     keyevent("KEYCODE_BACK")
#     sleep(1)
    
# 点击继续
# touch(agree_bt)
# sleep(1)

# # 进入我的界面
# touch(Template(r"tpl1629274844658.png", record_pos=(0.354, 0.814), resolution=(1080, 1920)))
# sleep(1)

# # 进入设置界面
# touch(Template(r"tpl1629274873255.png", record_pos=(0.422, -0.794), resolution=(1080, 1920)))
# sleep(2)
# ele_list = find_element_by_symbol(Template(r"tpl1629276407176.png", record_pos=(0.0, -0.794), resolution=(1080, 1920)), Template(r"tpl1629276435332.png", record_pos=(-0.39, -0.615), resolution=(1080, 1920)), Template(r"tpl1629276459770.png", record_pos=(-0.391, -0.116), resolution=(1080, 1920)), Template(r"tpl1629276484996.png", record_pos=(-0.39, 0.345), resolution=(1080, 1920)), Template(r"tpl1629279819991.png", record_pos=(-0.39, 0.719), resolution=(1080, 1920)))
# 点击问卷调查
# if ele_list[0] is not None:
#     touch(ele_list[0])
#     assert_exists_element(Template(r"tpl1629277476305.png", record_pos=(-0.018, -0.803), resolution=(1080, 1920)), "有奖调查打开成功", b_time=3, a_time=3)
#     keyevent("KEYCODE_BACK")
#     sleep(1)
# # 点击隐藏已完成图片
# if ele_list[1] is not None:
#     touch(ele_list[1])
#     sleep(1)
# # 点击填色阴影切换
# if ele_list[2] is not None:
#     touch(ele_list[2])
#     sleep(2)
#     touch(Template(r"tpl1629277758415.png", record_pos=(0.292, -0.519), resolution=(1080, 1920)))
#     sleep(1)
#     keyevent("KEYCODE_BACK")
    
# 点击商店按钮
# if ele_list[3] is not None:
#     touch(ele_list[3])
#     sleep(2)
#     swipe((527, 1563), (538, 65))
#     sleep(3)
#     touch((794, 706))
#     sleep(3)
#     touch(Template(r"tpl1629280156765.png", record_pos=(0.0, 0.694), resolution=(1080, 1920)))
#     sleep(3)
#     touch(Template(r"tpl1629280184723.png", record_pos=(0.002, 0.229), resolution=(1080, 1920)))
#     sleep(2)
    


# touch(Template(r"tpl1629274873255.png", record_pos=(0.422, -0.794), resolution=(1080, 1920)))
# sleep(2)

# if ele_list[3] is not None:
#     touch(ele_list[3])
#     sleep(2)
#     swipe((527, 1563), (538, 65))
#     sleep(3)
#     touch((794, 706))
#     sleep(3)
#     touch(Template(r"tpl1629280156765.png", record_pos=(0.0, 0.694), resolution=(1080, 1920)))
#     sleep(3)
#     touch(Template(r"tpl1629280184723.png", record_pos=(0.002, 0.229), resolution=(1080, 1920)))
#     sleep(2)
    

# touch(Template(r"tpl1629274873255.png", record_pos=(0.422, -0.794), resolution=(1080, 1920)))
# sleep(2)


# # 滑动列表
# swipe((500, 1344), (504, 153))
# sleep(2)

# ele_list = find_element_by_symbol(Template(r"tpl1629276407176.png", record_pos=(0.0, -0.794), resolution=(1080, 1920)), Template(r"tpl1629277958167.png", record_pos=(-0.391, -0.067), resolution=(1080, 1920)), Template(r"tpl1629277977418.png", record_pos=(-0.389, 0.086), resolution=(1080, 1920)), Template(r"tpl1629277991740.png", record_pos=(-0.389, 0.389), resolution=(1080, 1920)), Template(r"tpl1629278003613.png", record_pos=(-0.393, 0.546), resolution=(1080, 1920)))
# # 点击FAQ
# if ele_list[0] is not None:
#     touch(ele_list[0])
#     assert_exists_element(Template(r"tpl1629278428239.png", record_pos=(0.005, -0.706), resolution=(1080, 1920)), "FAQ进入成功", b_time=10)
#     keyevent("KEYCODE_BACK")
#     sleep(1)
    
# # 点击联系我们
# if ele_list[1] is not None:
#     touch(ele_list[1])
#     sleep(2)
#     touch(Template(r"tpl1629278671599.png", threshold=0.8500000000000001, record_pos=(-0.377, 0.622), resolution=(1080, 1920)))
#     sleep(3)
#     keyevent("KEYCODE_BACK")
#     sleep(1)
#     keyevent("KEYCODE_BACK")
    
# # 点击隐私协议
# if ele_list[2] is not None:
#     touch(ele_list[2])
#     sleep(10)
#     act_name = dev.get_top_activity_name()
#     assert_equal_element(act_name, "coloring.color.number.happy.paint.art.drawing.puzzle/talefun.cd.sdk.webview.MyWebViewActivity", "隐私协议链接是否正常跳出")
#     assert_exists_element(Template(r"tpl1629273292532.png", record_pos=(-0.311, -0.596), resolution=(1080, 1920)), "判断是否正常显示隐私协议页面")
#     keyevent("KEYCODE_BACK")
#     sleep(1)

# # 点击使用条款
# if ele_list[3] is not None:
#     touch(ele_list[3])
#     sleep(10)
#     act_name = dev.get_top_activity_name()
#     assert_equal_element(act_name, "coloring.color.number.happy.paint.art.drawing.puzzle/talefun.cd.sdk.webview.MyWebViewActivity", "隐私服务条款是否正常跳出")
#     assert_exists_element(Template(r"tpl1629273292532.png", record_pos=(-0.311, -0.596), resolution=(1080, 1920)), "判断是否正常显示服务条款页面")
#     keyevent("KEYCODE_BACK")
#     sleep(1)

# keyevent("KEYCODE_BACK")
# sleep(1)
# touch(Template(r"tpl1629279032067.png", record_pos=(-0.356, 0.813), resolution=(1080, 1920)))
# sleep(1)

# 进入图片
touch((280, 840))
sleep(10)
try:
    esdf=1
#     wait(Template(r"tpl1629345184802.png", record_pos=(-0.4, -0.802), resolution=(1080, 1920)), timeout=60)
except Exception as e:
    print("进图失败")
    raise e
else:
    import sys
    sys.path.append(r"C:\Users\xt875\Documents\airtest\LITE_airtest.air")
    from img_RGB2location_lite import RGB2LocationLite
    rgbLoc = RGB2LocationLite()
    rgbLoc.run_main()
    
    loc_list = find_element_by_symbol(Template(r"tpl1629351309582.png", record_pos=(0.0, 0.638), resolution=(1080, 1920)), Template(r"tpl1629351322633.png", record_pos=(-0.232, 0.356), resolution=(1080, 1920)), Template(r"tpl1629351337019.png", record_pos=(-0.002, 0.357), resolution=(1080, 1920)), Template(r"tpl1629351348992.png", record_pos=(0.231, 0.356), resolution=(1080, 1920)))
    
    # 点击收藏
    if loc_list[0] is not None:
        touch(loc_list[0])
        sleep(2)
        assert_exists_element(Template(r"tpl1629351451577.png", record_pos=(-0.232, 0.355), resolution=(1080, 1920)), "判定收藏成功")
        
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
        assert_exists_element(Template(r"tpl1629353665446.png", record_pos=(0.003, -0.187), resolution=(1080, 1920)), "分享弹窗弹出")
        keyevent("KEYCODE_BACK")
        
    # 点击继续回到主界面
    touch(Template(r"tpl1629346420050.png", record_pos=(-0.001, 0.638), resolution=(1080, 1920)))

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




    
