# -*- encoding=utf8 -*-
__author__ = "xt875"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.android.android import Android


class UserSkip():
    def __init__(self):
        self.terms_link = wait(Template(r"tpl1626070061249.png", record_pos=(-0.196, 0.058), resolution=(1080, 1920)))
        self.privacy_link = wait(Template(r"tpl1626070077012.png", record_pos=(0.188, 0.06), resolution=(1080, 1920)))
        self.continue_bt = wait(Template(r"tpl1626070101392.png", record_pos=(0.009, 0.347), resolution=(1080, 1920)))
        
    def secondary_menu(self):
        self.vioce_bt = wait(Template(r"tpl1626070175139.png", record_pos=(0.419, -0.678), resolution=(1080, 1920)))
        self.music_bt = wait(Template(r"tpl1626070797272.png", record_pos=(0.421, -0.562), resolution=(1080, 1920)))
        self.restart_bt = wait(Template(r"tpl1626070905945.png", record_pos=(0.421, -0.448), resolution=(1080, 1920)))
        self.home_bt = wait(Template(r"tpl1626070920784.png", record_pos=(0.42, -0.325), resolution=(1080, 1920)))
        
    def __exit_menu(self):
        self.close_bt = wait(Template(r"close.png", record_pos=(0.425, -0.549), resolution=(1080, 1920)))
        self.cancel_bt = wait(Template(r"tpl1626071462020.png", record_pos=(-0.206, 0.19), resolution=(1080, 1920)))
        self.exit_bt = wait(Template(r"tpl1626071531930.png", record_pos=(0.276, 0.189), resolution=(1080, 1920)))


        
    def __restart_page(self, pause_bt):
        self.__click(pause_bt, 2)
        self.__click(self.restart_bt, 2)
        self.__exit_menu()
        assert_exists(Template(r"tpl1626071258135.png", record_pos=(0.004, -0.462), resolution=(1080, 1920)), "重玩弹窗是否正常跳出")
        
    def __exit_page(self, pause_bt):
        self.__click(pause_bt, 2)
        self.__click(self.home_bt, 2)
        self.__exit_menu()
        assert_exists(Template(r"tpl1626072266371.png", record_pos=(-0.001, -0.46), resolution=(1080, 1920)), "返回主界面弹窗是否正常跳出")



    def __click(self, bt_location, timeout=0):
        sleep(timeout)
        touch(bt_location)
        
    def __double_click(self, bt, timeout=0.05):
        touch(bt)
        sleep(timeout)
        touch(bt)
        
        
    def run_skip(self):
        dev = Android()
        # 点击服务条款链接
        self.__click(self.terms_link, 5)
        act_name = dev.get_top_activity_name()
        print(act_name)
        assert_equal(act_name, "com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity", "服务条款链接是否正常跳出")
        
        keyevent("KEYCODE_BACK")
        # 点击隐私协议链接
        self.__click(self.privacy_link, 5)
        act_name = dev.get_top_activity_name()
        assert_equal(act_name, "com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity", "隐私协议链接是否正常跳出")
        
        keyevent("KEYCODE_BACK")
        # 点击继续按钮
        self.__click(self.continue_bt)
        # 判断是否存在账号同步弹窗
        if exists(Template(r"tpl1626145203687.png", record_pos=(0.012, -0.614), resolution=(1080, 1920))):
            self.__click(wait(Template(r"close.png", record_pos=(0.425, -0.549), resolution=(1080, 1920))), 2)


            pause_bt = wait(Template(r"tpl1626854418664.png", record_pos=(0.423, -0.798), resolution=(1080, 1920)))
            self.__click(pause_bt, 2)
        else:
            pause_bt = wait(Template(r"tpl1626854418664.png", record_pos=(0.423, -0.798), resolution=(1080, 1920)))
            # 点击暂停按钮
            self.__double_click(pause_bt, 1)
        # self.__click(pause_bt, 2)
        # 调用二级菜单初始化
        self.secondary_menu()
        
        # 点击 音量按钮
        self.__click(self.vioce_bt, 2)
        self.__click(self.vioce_bt, 2)
        # 点击音乐按钮
        self.__click(self.music_bt, 2)
        self.__click(self.music_bt, 2)
        # 容错
        self.__click(pause_bt, 2)
        # 点击重玩按钮
        self.__restart_page(pause_bt)
        # 重玩取消
        self.__click(self.cancel_bt, 2)
        # 点击重玩按钮
        self.__restart_page(pause_bt)
        # 点击重玩关闭
        self.__click(self.close_bt, 2)
        # 点击重玩按钮
        self.__restart_page(pause_bt)
        # 点击重玩
        self.__click(self.exit_bt, 2)
        self.__click(wait(Template(r"tpl1626071976783.png", record_pos=(-0.206, 0.197), resolution=(1080, 1920))), 2)
        # 容错
        self.__click(pause_bt, 2)
        # 点击退出
        self.__exit_page(pause_bt)
        # 点击取消
        self.__click(self.cancel_bt, 2)
        # 点击退出
        self.__exit_page(pause_bt)
        # 点击关闭
        self.__click(self.close_bt, 2)
        # 点击退出
        self.__exit_page(pause_bt)
        # 点击返回主界面
        self.__click(self.exit_bt, 2)
        

user_skip = UserSkip()



