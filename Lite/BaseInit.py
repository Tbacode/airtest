'''
 * @Descripttion : 
 * @Author       : Tommy
 * @Date         : 2021-09-01 15:04:09
 * @LastEditors  : Tommy
 * @LastEditTime : 2021-09-03 14:24:33
'''
# -*- encoding=utf8 -*-
__author__ = "Tommy"

from airtest.core.api import *
from airtest.core.android.android import Android
from airtest.cli.parser import cli_setup


class baseInit(object):

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
                local = wait_element(item_ele)
                local_list.append(local)
        return local_list

    # 游戏启动初始化
    def init(self, packagename="coloring.color.number.happy.paint.art.drawing.puzzle", flag=1):
        dev = Android()
        if flag == 1:
            dev.clear_app(packagename)
            if not dev.is_locked():
                dev.unlock()
        dev.start_app(packagename)
        return dev

    # 进入成功判定
    def is_enter_home(self, flag=1, timeout=10):
        sleep(timeout)
        if flag == 1:
            if exists(Template(r"../tpl1629269284035.png", record_pos=(-0.001, -0.379), resolution=(1080, 1920))):
                agree_bt = self.wait_element(Template(
                    r"../tpl1629279181598.png", record_pos=(-0.004, 0.193), resolution=(1080, 1920)))
                terms_link = self.wait_element(Template(
                    r"../tpl1629279205859.png", record_pos=(-0.149, -0.012), resolution=(1080, 1920)))
                print(terms_link)
                privacy_link = self.wait_element(Template(
                    r"../tpl1629279228084.png", record_pos=(0.061, -0.013), resolution=(1080, 1920)))
                print(privacy_link)
                return agree_bt, terms_link, privacy_link
            else:
                self.is_enter_home()
        else:
            print("非首次进入判定节点进入")
            sleep(timeout)
            if not exists(Template(r"../tpl1630578345457.png", record_pos=(-0.369, -0.377), resolution=(1080, 1920))):
                timeout = 3
                self.is_enter_game(2, timeout)
