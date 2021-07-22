# -*- encoding=utf8 -*-
__author__ = "xt875"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.android.android import Android
from datetime import datetime




# script content
print("start...")
class LevelFinish():
    def __init__(self, packagename):
        self.dev = Android()
        self.packagename = packagename

    def finish_judge(self):
        if exists(Template(r"tpl1626851207378.png", record_pos=(-0.003, -0.194), resolution=(1080, 1920))):
            print("关卡通过判定成功")
            return True
        return False

    def level_finish(self, timeout=5):
        sleep(timeout)
        if self.finish_judge():
            touch(Template(r"tpl1626851365025.png", record_pos=(0.002, 0.383), resolution=(1080, 1920)))
        else:
            touch(Template(r"tpl1626851406900.png", record_pos=(-0.377, -0.805), resolution=(1080, 1920)))
            sleep(5)
            self.level_finish(3)

    def level_start(self, is_tips="no", tips_img=None, tips_msg=None):
        if is_tips == "yes":
            touch((555, 1400))
            sleep(1)
            if exists(Template(r"tpl1626851703876.png", record_pos=(0.006, 0.372), resolution=(1080, 1920))):
                touch(Template(r"tpl1626851703876.png", record_pos=(0.006, 0.372), resolution=(1080, 1920)))
                sleep(4)
                assert_exists(tips_img, tips_msg)
                touch((530,50))
        else:
            touch((555, 1400))
            sleep(1)
            if exists(Template(r"tpl1626851703876.png", record_pos=(0.006, 0.372), resolution=(1080, 1920))):
                touch(Template(r"tpl1626851703876.png", record_pos=(0.006, 0.372), resolution=(1080, 1920)))
                sleep(4)



    def level_enter_judge(self):
        if exists(Template(r"tpl1626854418664.png", record_pos=(0.323, -0.781), resolution=(1080, 1920))):
            return True
        else:
            return False
        
        
    def is_gameActivity_top(self):
        if str(self.dev.get_top_activity_name())




    def run_level_main(self):
        # 第一关
        if self.level_enter_judge():
            swipe((535, 1100), (90, 1045), duration=2)
            self.level_finish()
            sleep(5)
            touch(Template(r"close.png", record_pos=(0.361, -0.617), resolution=(1080, 1920)))
        else:
            return "关卡1，进入失败"
        # 2
        self.level_start("yes", Template(r"tpl1626854804508.png", record_pos=(0.004, -0.527), resolution=(1080, 1920)), "判断是否弹出炸弹引导遮罩层")
        if self.level_enter_judge():
            swipe((535, 1270), (956, 1270), duration=2)
            self.level_finish(15)
            sleep(5)
        else:
            return "关卡2，进入失败"
            
        # 3
        self.level_start("yes", Template(r"tpl1626855250121.png", record_pos=(-0.006, -0.463), resolution=(1080, 1920)), "判断激光砖块tips引导遮罩层")
        if self.level_enter_judge():
            touch((540, 500), duration=2)
            self.level_finish()
            sleep(5)
        else:
            return "关卡3，进入失败"    
        # 4
        self.level_start()
        if self.level_enter_judge():
            swipe((535, 1225), (160, 1225), duration=2)
            self.level_finish(15)
            sleep(5)
        else:
            return "关卡4，进入失败"
        
        # reward引导
        touch((590, 275))
        sleep(2)
        touch(Template(r"tpl1626856059431.png", record_pos=(0.0, 0.786), resolution=(1080, 1920)))
        sleep(1)
        
        # 5
        self.level_start("yes", Template(r"tpl1626854804508.png", record_pos=(0.004, -0.527), resolution=(1080, 1920)), "判断气泡砖块引导遮罩层")
        if self.level_enter_judge():
            swipe((550, 1200), (135, 1200), duration=2)
            self.level_finish(10)
            sleep(5)
        else:
            return "关卡5， 进入失败"
        
        # 6
        self.level_start("yes", Template(r"tpl1626855250121.png", record_pos=(-0.006, -0.463), resolution=(1080, 1920)), "判断分岔砖块引导tips")
        if self.level_enter_judge():
            touch((535, 440), duration=2)
            self.level_finish(10)
            sleep(5)
        else:
            return "关卡6， 进入失败"
        
        # 7
        self.level_start()
        if self.level_enter_judge():
            swipe((535, 1120), (1005, 1140), duration=2)
            sleep(5)
            if exists(Template(r"tpl1626859183935.png", record_pos=(0.261, 0.578), resolution=(1080, 1920))):
                touch((970, 1787))
            self.level_finish()
            sleep(5)
        else:
            return "关卡7， 进入失败"
        
        # 8
        self.level_start("yes", Template(r"tpl1626854804508.png", record_pos=(0.004, -0.527), resolution=(1080, 1920)), "判断炸弹消除砖块引导遮罩层")
        if self.level_enter_judge():
            swipe((550, 1190), (40, 1172), duration=2)
            self.level_finish()
            sleep(5)
        else:
            return "关卡8， 进入失败"
        
        # 9
        self.level_start("yes", Template(r"tpl1626859508189.png", record_pos=(0.002, -0.544), resolution=(1080, 1920)), "判断新道具引导遮罩层")
        touch((140, 1800))
        sleep(2)
        touch((536, 828))
        sleep(2)
        if self.level_enter_judge():
            touch((540, 745), duration=2)
            self.level_finish(15)
            sleep(5)
        else:
            return "关卡9， 进入失败"
        
        touch(Template(r"close.png", record_pos=(0.361, -0.617), resolution=(1080, 1920)))
        
        # 10
        
        self.level_start()
        if self.level_enter_judge():
            swipe((540,1163), (102, 1120), duration=2)
            self.level_finish()
            sleep(5)
        else:
            return "关卡10， 进入失败"
        
        # 11
        self.level_start("yes", Template(r"tpl1626859508189.png", record_pos=(0.002, -0.544), resolution=(1080, 1920)), "判断新道具引导遮罩层")
        touch((400, 1800))
        sleep(3)
        touch((530, 1260))
        sleep(3)
        if self.level_enter_judge():
            touch((116, 1244), duration=2)
            self.level_finish(15)
            sleep(5)
        else:
            return "关卡11， 进入失败"
        
        # 12
        self.level_start()
        if self.level_enter_judge():
            touch((60, 1255), duration=2)
            self.level_finish(15)
            sleep(5)
        else:
            return "关卡12， 进入失败"
        
        # 13
        self.level_start("yes", Template(r"tpl1626859508189.png", record_pos=(0.002, -0.544), resolution=(1080, 1920)), "判断新道具引导遮罩层")
        touch((670, 1800))
        sleep(3)
        if self.level_enter_judge():
            touch((106, 1073), duration=2)
            self.level_finish(8)
            sleep(5)
        else:
            return "关卡13， 进入失败"
        
        # 评论引导弹窗
        if exists(Template(r"tpl1626926086185.png", record_pos=(0.019, -0.269), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1626926086185.png", record_pos=(0.019, -0.269), resolution=(1080, 1920)), "评论引导弹窗弹出")
            touch(Template(r"tpl1626926276626.png", record_pos=(0.018, 0.355), resolution=(1080, 1920)))
            act_name = self.dev.get_top_activity_name()
            assert_equal(act_name, "com.android.vending/com.google.android.finsky.activities.MainActivity", "评论跳出成功检测")
            sleep(2)
            keyevent("KEYCODE_BACK")
            
        # 14
        self.level_start()
        if self.level_enter_judge():
            touch((75, 1140), duration=2)
            self.level_finish(15)
            sleep(5)
        else:
            return "关卡14， 进入失败"
        
        # 判断星期三的活动奖励
        if str(datetime.now().isoweekday()) == "4":
            assert_exists(Template(r"tpl1626336292054.png", record_pos=(0.003, -0.535), resolution=(1080, 1920)), "周4活动奖励弹出检测")
            touch(Template(r"claim.png", record_pos=(-0.004, 0.457), resolution=(1080, 1920)))
            sleep(2)
        
        # 15
        self.level_start("yes", Template(r"tpl1626854804508.png", record_pos=(0.004, -0.527), resolution=(1080, 1920)), "判断木板砖块引导遮罩层")
        if self.level_enter_judge():
            touch((71, 830), duration=2)
            self.level_finish(10)
            sleep(5)
        else:
            return "关卡15， 进入失败"


            
        


levelfinish = LevelFinish("com.brick.breaker.ball.shooting.blast")
