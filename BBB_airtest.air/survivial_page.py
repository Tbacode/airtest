# -*- encoding=utf8 -*-
__author__ = "xt875"

from airtest.core.api import *


class SurvivialPage():
    def __init__(self):
        self.rabbit = wait(Template(r"tpl1626241664084.png", record_pos=(-0.156, -0.041), resolution=(1080, 1920)))
        
    def __click(self, bt, timeout=0):
        sleep(timeout)
        touch(bt)
        
    def __quit(self):
        sleep(3)
        pause_bt = wait(Template(r"tpl1626854418664.png", record_pos=(0.423, -0.798), resolution=(1080, 1920)))
        self.__click(pause_bt, 2)
        home_bt = wait(Template(r"tpl1626241887157.png", record_pos=(0.285, -0.375), resolution=(1080, 1920)))
        self.__click(home_bt, 2)
        assert_exists(Template(r"tpl1626241918048.png", record_pos=(0.004, -0.474), resolution=(1080, 1920)), "冒险退出弹窗是否正常弹出")
        quit_bt = wait(Template(r"tpl1626241950060.png", record_pos=(0.0, 0.255), resolution=(1080, 1920)))
        self.__click(quit_bt, 2)
        
    def run_survivial(self):
        self.__click(self.rabbit, 2)
        self.__quit()
        # 关闭
        close_bt = wait(Template(r"close.png", record_pos=(0.365, -0.477), resolution=(1080, 1920)))
        self.__click(close_bt, 1)
        # 再次进入
        self.__click(self.rabbit, 2)
        self.__quit()
        # 重试
        retry_bt = wait(Template(r"tpl1626242316937.png", record_pos=(-0.202, 0.256), resolution=(1080, 1920)))
        self.__click(retry_bt, 2)
        sleep(2)
        self.__quit()
        # 退出
        exit_bt = wait(Template(r"tpl1626242381986.png", record_pos=(0.203, 0.253), resolution=(1080, 1920)))
        self.__click(exit_bt,2)
        
        
survivial = SurvivialPage()



        

