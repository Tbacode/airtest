'''
Author: your name
Date: 2021-07-06 15:32:34
LastEditTime: 2021-07-08 10:59:53
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \air脚本\BBB_airtest.air\settingpage.py
'''
# -*- encoding=utf8 -*-
__author__ = "xt875"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.android.android import Android




# script content
class SettingPage():
    
    def __init__(self):
        self.music_bt = wait(Template(r"tpl1625482014718.png", record_pos=(-0.128, -0.444), resolution=(1080, 1920)))
        self.voice_bt = wait(Template(r"tpl1625482106339.png", record_pos=(0.129, -0.447), resolution=(1080, 1920)))
        self.language_bt = wait(Template(r"tpl1625482153572.png", record_pos=(0.001, -0.264), resolution=(1080, 1920)))

        self.terms_bt = wait(Template(r"tpl1625712828283.png", record_pos=(0.003, -0.102), resolution=(1080, 1920)))

        self.privacy_bt = wait(Template(r"tpl1625712843601.png", record_pos=(-0.001, 0.064), resolution=(1080, 1920)))

        self.contact_bt = wait(Template(r"tpl1625712858434.png", record_pos=(0.0, 0.231), resolution=(1080, 1920)))

        self.save_bt = wait(Template(r"tpl1627889922603.png", record_pos=(0.004, 0.405), resolution=(1080, 1920)))



        self.close_bt = wait(Template(r"close.png", record_pos=(0.41, -0.569), resolution=(1080, 1920)))
    def __double_click(self, bt, timeout=0.05):
        touch(bt)
        sleep(timeout)
        touch(bt)

    def __click(self, bt_location, timeout=0):
        sleep(timeout)
        touch(bt_location)
        
    def __return_en_language(self):
        self.__click(self.language_bt, 1)
        self.__click(wait(Template(r"tpl1625560229998.png", record_pos=(-0.006, -0.542), resolution=(1080, 1920))), 2)
        self.__click(Template(r"close.png", record_pos=(0.41, -0.569), resolution=(1080, 1920)), 1)
        
    def run_setpage(self):
        self.__click(self.music_bt, 1)
        self.__click(self.voice_bt, 1)
        self.__click(self.language_bt)

        self.__click(Template(r"tpl1625558654442.png", record_pos=(-0.005, 0.663), resolution=(1080, 1920)), 2)
        assert_exists(Template(r"tpl1625559138816.png", record_pos=(-0.002, -0.706), resolution=(1080, 1920)), "语言是否切换成功")

        self.__click(Template(r"close.png", record_pos=(0.41, -0.569), resolution=(1080, 1920)), 2)
        self.__return_en_language()
        # 点击条款链接
        self.__click(self.terms_bt, 2)
        sleep(5)
        dev = Android()
        act_name = dev.get_top_activity_name()
        
        assert_equal(act_name, "com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity", "服务条款按钮是否正常跳出")
        sleep(2)
        keyevent("KEYCODE_BACK")
        # 点击隐私链接
        self.__click(self.privacy_bt, 2)
        sleep(5)
        act_name = dev.get_top_activity_name()
        
        assert_equal(act_name, "com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity", "隐私协议按钮是否正常跳出")
        sleep(2)
        keyevent("KEYCODE_BACK")
        # 点击联系我们
        self.__click(self.contact_bt)
        act_name = dev.get_top_activity_name()
        sleep(2)
        assert_equal(act_name, "com.google.android.gm/.ComposeActivityGmailExternal", "邮件弹窗是否正常弹出")
        dev.start_app("com.brick.breaker.ball.shooting.blast") # 进入邮箱后，返回不能回到游戏，直接调用start方法进入游戏
        # 点击开启fb登录弹窗
        self.__click(self.save_bt, 2)
        fb_bt = wait(Template(r"tpl1628678204243.png", record_pos=(0.001, 0.27), resolution=(1080, 1920)))

        self.__click(fb_bt, 2)
#         assert_exists(Template(r"tpl1625723667791.png", record_pos=(0.0, -0.469), resolution=(1080, 1920)), "fb登录成功")
#         # 替换固定资源图片
#         self.__click(Template(r"close.png", record_pos=(0.41, -0.569), resolution=(1080, 1920)), 2)
        load_success = wait(Template(r"tpl1625723780790.png", record_pos=(0.206, 0.287), resolution=(1080, 1920)))
        self.__click(load_success, 2)
        confirm_text = wait(Template(r"tpl1625723856907.png", record_pos=(-0.006, -0.274), resolution=(1080, 1920)))
        self.__click(confirm_text)
        text("CONFIRM")
        ok_bt = wait(Template(r"tpl1625723954769.png", record_pos=(0.208, -0.055), resolution=(1080, 1920)))
        # dev.double_click(ok_bt)
        self.__double_click(ok_bt, 2)





        
        

set_page = SettingPage()
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)




