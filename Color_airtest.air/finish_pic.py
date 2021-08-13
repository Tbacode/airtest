# -*- encoding=utf8 -*-
__author__ = "xt875"

from airtest.core.api import *




# script content
print("start...")

class FinishPic():
    def __init__(self):
        self.x_start = 60
        self.x_end = 1015
        self.y_start = 334
        self.y_end = 1289
        self.step = 20
    
    def touch_init(self):
        touch((544, 813))
        sleep(2)
        touch((977, 1390))
        sleep(2)
        
    def touch_for_finishPic(self):
        sleep(2)
        if exists(Template(r"tpl1628064553858.png", record_pos=(0.281, -0.797), resolution=(1080, 1920))):
            touch((125, 1635))
            for x in range(self.x_start, self.x_end + 1, self.step):
                for y in range(self.y_start, self.y_end + 1, self.step):
                    touch((x + self.step/2, y + self.step/2))
                    print("点击坐标点：", str((x + self.step/2, y + self.step/2)))
                    # sleep(1)
            self.touch_for_finishPic()
                    
                    
fp = FinishPic()

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)