# -*- encoding=utf8 -*-
__author__ = "talefun"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.android.android import Android

class baseInit(object):
    
    # 进入成功判定
    def is_enter_home(self, flag=1, timeout=10):
        
        if flag == 1:
            sleep(timeout)
            if exists(Template(r"../tpl1628762015501.png", record_pos=(-0.005, -0.243), resolution=(1080, 1920))):
                agree_bt = self.wait_element(Template(r"../tpl1628062510559.png", record_pos=(0.002, 0.304), resolution=(1080, 1920)))
                terms_link = self.wait_element(Template(r"../tpl1628062685346.png", record_pos=(-0.169, 0.099), resolution=(1080, 1920)))
                privacy_link = self.wait_element(Template(r"../tpl1628062704363.png", record_pos=(0.022, 0.095), resolution=(1080, 1920)))
                return agree_bt, terms_link, privacy_link
            else:
                timeout = 3
                self.is_enter_home(1, timeout)
        else:
            print("非首次进入判定节点进入")
            sleep(timeout)
            if not exists(Template(r"../tpl1630654913186.png", record_pos=(-0.342, -0.387), resolution=(1080, 1920))):
                timeout = 3
                self.is_enter_home(2, timeout)
            
    # 断言元素是否存在
    def assert_exists_element(self, element, ass_msg, b_time=0, a_time=0):
        sleep(b_time)
        try:
            assert_exists(element, ass_msg)
        except AssertionError as f:
            print("元素断言不存在，异常")
        sleep(a_time)

    # 断言元素是否相等
    def assert_equal_element(self, element, ass_element, ass_msg, b_time=0, a_time=0):
        sleep(b_time)
        try:
            assert_equal(element, ass_element, ass_msg)
        except AssertionError as f:
            print("元素断言不相等，异常")
        sleep(a_time)

    # 等待元素出现
    def wait_element(self, element, timeout=20, b_time=0, a_time=0):
        sleep(b_time)
        try:
            location = wait(element, timeout=timeout)
        except TargetNotFoundError as t:
            print("找不到该元素")
            location = None
        sleep(a_time)
        return location
    
    # 以参照物（sym_ele）寻找多个元素
    def find_element_by_symbol(self, sym_ele, *args):
        local_list = []
        if exists(sym_ele):
            for item_ele in args:
                local = self.wait_element(item_ele)
                local_list.append(local)
        return local_list
    
    # 游戏启动初始化
    def init(self, packagename="com.pixel.art.coloring.by.number", flag=1):
        dev = Android()
        if flag == 1:
            print("初始化游戏启动")
            dev.clear_app(packagename)
            if not dev.is_locked():
                dev.unlock()
        dev.start_app(packagename)
        return dev
    
    # 游戏退出,官方API会导致游戏数据写入失败，与预期不符
    def exit_game(self, b_timeout=0, a_timeout=0):
        sleep(b_timeout)
        keyevent("KEYCODE_BACK")
        sleep(2)
        yes_bt = self.wait_element(Template(r"../tpl1630999512618.png", record_pos=(-0.163, 0.319), resolution=(1080, 1920)))
        if yes_bt is not None:
            touch(yes_bt)


