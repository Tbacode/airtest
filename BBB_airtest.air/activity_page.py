# -*- encoding=utf8 -*-
__author__ = "xt875"

from airtest.core.api import *
from datetime import datetime

class ActivityPage():    
    def __init__(self):
        self.dayOfweek = str(datetime.now().isoweekday())
        self.week_act_dict = {
            "1": {"img_bt":Template(r"tpl1626675215412.png", record_pos=(-0.385, -0.415), resolution=(1080, 1920)), "assert_img":Template(r"tpl1626675233284.png", record_pos=(-0.002, -0.531), resolution=(1080, 1920))},
            "2": {"img_bt":Template(r"tpl1626753717895.png", record_pos=(-0.381, -0.415), resolution=(1080, 1920)), "assert_img":Template(r"tpl1626753732349.png", record_pos=(0.0, -0.527), resolution=(1080, 1920))},
            "3": {"img_bt":Template(r"tpl1626253495511.png", record_pos=(-0.381, -0.185), resolution=(1080, 1920)), "assert_img":Template(r"tpl1626254570274.png", record_pos=(0.006, -0.537), resolution=(1080, 1920))},
            "4": {"img_bt":Template(r"tpl1626336268506.png", record_pos=(-0.384, -0.413), resolution=(1080, 1920)), "assert_img":Template(r"tpl1626336292054.png", record_pos=(0.003, -0.535), resolution=(1080, 1920))},
            "5": {"img_bt":Template(r"tpl1626415428434.png", record_pos=(-0.384, -0.408), resolution=(1080, 1920)), "assert_img":Template(r"tpl1626415451780.png", record_pos=(-0.003, -0.535), resolution=(1080, 1920))},
            "6": {"img_bt":"", "assert_img":""},
            "7": {"img_bt":"", "assert_img":""}
        }
        
    def __return_img_dict(self):

        return self.week_act_dict[self.dayOfweek]
    
    def run_activity(self):
        img_dict = self.__return_img_dict()
        return img_dict
    


act = ActivityPage()
