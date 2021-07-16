# -*- encoding=utf8 -*-
__author__ = "xt875"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.android.android import Android




# script content
class ShopPage():
    def __init__(self):
        
        self.jp_340_bt = wait(Template(r"tpl1626156136994.png", record_pos=(0.269, -0.663), resolution=(1080, 1920)))
        self.dev = Android()
        
    def __click(self, bt, timeout=0):
        sleep(timeout)
        touch(bt)
        
    def __click_pay(self):
        # 购买jp340
        self.__click(self.jp_340_bt, 2)
        sleep(3)
        # 支付弹窗验证
        google_pay = self.dev.get_top_activity_name()
        assert_equal(google_pay, "com.android.vending/com.google.android.finsky.billing.acquire.SheetUiBuilderHostActivity", "google支付弹窗是否正常")
        
    def run_shop(self):
        if exists(Template(r"tpl1626156645965.png", record_pos=(0.003, 0.036), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1626156945964.png", record_pos=(0.004, 0.037), resolution=(1080, 1920)), "进入商店页面是否正常")
        # 支付调用
        self.__click_pay()
        # 支付取消
        keyevent("KEYCODE_BACK")
        assert_exists(Template(r"tpl1626157458059.png", record_pos=(0.004, -0.456), resolution=(1080, 1920)), "支付失败弹窗是否正常弹出")
        self.__click(wait(Template(r"tpl1626157483302.png", record_pos=(0.006, 0.208), resolution=(1080, 1920))), 2)
        # 支付调用
        self.__click_pay()
        self.__click(wait(Template(r"tpl1626157754670.png", record_pos=(0.004, 0.692), resolution=(1080, 1920))), 2)
        assert_exists(Template(r"tpl1626157781294.png", record_pos=(-0.008, -0.616), resolution=(1080, 1920)), "支付成功弹窗是否正常弹出")
        self.__click((50,50),3)





        
        
shop = ShopPage()


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)