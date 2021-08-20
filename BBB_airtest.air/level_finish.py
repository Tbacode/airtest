# -*- encoding=utf8 -*-
__author__ = "xt875"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.android.android import Android
from datetime import datetime

import cv2
import os
import numpy as np

# script content
print("start...")


class LevelFinish():
    def __init__(self, packagename):
        self.dev = Android()
        self.packagename = packagename
        self.index = 1

    def finish_judge(self):
        if exists(
                Template(r"tpl1626851207378.png",
                         record_pos=(-0.003, -0.194),
                         resolution=(1080, 1920))):
            print("关卡通过判定成功")
            return True
        return False

    def level_finish(self, timeout=5):
        sleep(timeout)
        if self.finish_judge():
            touch(
                Template(r"tpl1626851365025.png",
                         record_pos=(0.002, 0.383),
                         resolution=(1080, 1920)))
            self.index += 1
            print("-----level_num" + str(self.index))
            sleep(3)
            if self.index == 20:
                sleep(3)
                self.is_gameActivity_top()
                try:
                    assert_exists(Template(r"tpl1627458115954.png", record_pos=(0.021, 0.257), resolution=(1080, 1920)), "判断小猪银行弹出时机")
                except:
                    print("小猪银行弹出失败")
                else:
                    touch(Template(r"close.png",
                                 record_pos=(0.361, -0.617),
                                 resolution=(1080, 1920)))
                    sleep(1)
            if self.index == 30:
                sleep(4)
                if exists(Template(r"tpl1627019953062.png",
                                 record_pos=(0.003, -0.67),
                                 resolution=(1080, 1920))):
                    print(str(self.index) + "进入关卡数")
                    touch(Template(r"close.png",
                                 record_pos=(0.361, -0.617),
                                 resolution=(1080, 1920)))
                    sleep(1)
        else:
#             touch(
#                 Template(r"tpl1626851406900.png",
#                          record_pos=(-0.377, -0.805),
#                          resolution=(1080, 1920)))
#             sleep(5)
            self.level_finish(3)

    def level_start(self,
                    is_tips="no",
                    tips_img=None,
                    tips_msg=None,
                    timeout=4):
        if is_tips == "yes":
            touch((555, 1400))
            sleep(1)
            if exists(
                    Template(r"tpl1626851703876.png",
                             record_pos=(0.006, 0.372),
                             resolution=(1080, 1920))):
                touch(
                    Template(r"tpl1626851703876.png",
                             record_pos=(0.006, 0.372),
                             resolution=(1080, 1920)))
                assert_exists(tips_img, tips_msg)
                touch((530, 50))

                sleep(timeout)
        else:
            touch((555, 1400))
            sleep(1)
            if exists(
                    Template(r"tpl1626851703876.png",
                             record_pos=(0.006, 0.372),
                             resolution=(1080, 1920))):
                touch(
                    Template(r"tpl1626851703876.png",
                             record_pos=(0.006, 0.372),
                             resolution=(1080, 1920)))
                sleep(timeout)

    def level_enter_judge(self):
        if exists(
                Template(r"tpl1626854418664.png",
                         record_pos=(0.323, -0.781),
                         resolution=(1080, 1920))) or exists(
                             Template(r"tpl1626945205643.png",
                                      record_pos=(0.325, -0.778),
                                      resolution=(1080, 1920))):
            return True
        else:
            return False

    def is_gameActivity_top(self):
        index = 0
        sleep(3)
        print(self.dev.get_top_activity_name())
        if "com.unity3d.player.MainActivity" not in str(
                self.dev.get_top_activity_name()):
            home()
            sleep(2)
            start_app(self.packagename)
            sleep(2)
            if exists(Template(r"tpl1626945604308.png",
                             record_pos=(0.008, -0.63),
                             resolution=(1080, 1920))):
                touch(
                    Template(r"close.png",
                             record_pos=(0.361, -0.617),
                             resolution=(1080, 1920)))
                
    def crop_img(self):
        print("进入裁剪")
        Img = cv2.imread(r"C:/Users/xt875/Documents/airtest/BBB_airtest.air/screen_bbb_air.jpg")
        cropped = Img[1430:1630, 35:1040] # 裁剪坐标为[y0:y1, x0:x1]
        cv2.imwrite("C:/Users/xt875/Documents/airtest/BBB_airtest.air/screen_bbb_air_crop.jpg", cropped)
#         return "C:/Users/xt875/Documents/airtest/Color_airtest.air/screen_air_crop.jpg"

    def get_location_node(self, numb):
        self.crop_img()
        Img = cv2.imread("C:/Users/xt875/Documents/airtest/BBB_airtest.air/screen_bbb_air_crop.jpg")  #读入一幅图像
        

        # kernel_2 = np.ones((1, 1), np.uint8)  #2x2的卷积核

        # kernel_3 = np.ones((3, 3), np.uint8)  #3x3的卷积核

        # kernel_4 = np.ones((4, 4), np.uint8)  #4x4的卷积核
        kernel_2 = self.set_kernel(numb)

        if Img is not None:  #判断图片是否读入

            HSV = cv2.cvtColor(Img, cv2.COLOR_BGR2HSV)  #把BGR图像转换为HSV格式
        '''

        HSV模型中颜色的参数分别是：色调(H)，饱和度(S)，明度(V)

        下面两个值是要识别的颜色范围

        '''

        Lower = np.array([0, 0, 245])  #要识别颜色的下限

        Upper = np.array([0, 0, 254])  #要识别的颜色的上限

        #mask是把HSV图片中在颜色范围内的区域变成白色，其他区域变成黑色

        mask = cv2.inRange(HSV, Lower, Upper)

        #下面四行是用卷积进行滤波

        erosion = cv2.erode(mask, kernel_2, iterations=1)

        erosion = cv2.erode(erosion, kernel_2, iterations=1)

        dilation = cv2.dilate(erosion, kernel_2, iterations=1)

        dilation = cv2.dilate(dilation, kernel_2, iterations=1)

        #target是把原图中的非目标颜色区域去掉剩下的图像

        target = cv2.bitwise_and(Img, Img, mask=dilation)

        #将滤波后的图像变成二值图像放在binary中

        ret, binary = cv2.threshold(dilation, 127, 255, cv2.THRESH_BINARY)

        #在binary中发现轮廓，轮廓按照面积从小到大排列

        # cv2.imshow("binary", binary)

        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_SIMPLE)

        # print("++++++++contours", contours)
        p = 0
        node_list = []

        for i in contours:  #遍历所有的轮廓

            x, y, w, h = cv2.boundingRect(i)  #将轮廓分解为识别对象的左上角坐标和宽、高

            #在图像上画上矩形(图片、左上角坐标、右下角坐标、颜色、线条宽度)

            cv2.rectangle(Img, (x, y), (x + w, y + h), (0,255,), 3)

            # 输出图像矩形中间坐标点
            # print("中心坐标：{0},{1}".format(str(x+w/2), str(y+h/2)))
            # print((x + w / 2, y + h / 2))
            node_list.append((x + w / 2, y + h / 2))

            #给识别对象写上标号

            font = cv2.FONT_HERSHEY_SIMPLEX

            cv2.putText(Img, str(p), (x - 10, y + 10), font, 1, (0, 0, 255),
                        2)  #加减10是调整字符位置

            p += 1

            # print ('黄色方块的数量是',p,'个')#终端输出目标数量

            # cv2.imshow('target', target)

            # cv2.imshow('Mask', mask)

            # cv2.imshow("prod", dilation)

            # cv2.imshow('Img', Img)

        cv2.imwrite('Img.png', Img)  #将画上矩形的图形保存到当前目录
        return node_list
    
    def get_app_img(self):
        os.system(r"adb shell screencap -p /sdcard/screen_bbb_air.jpg")
        self.push_img2devices()
    def push_img2devices(self):
        os.system(r"adb pull /sdcard/screen_bbb_air.jpg C:/Users/xt875/Documents/airtest/BBB_airtest.air/screen_bbb_air.jpg")

    def set_kernel(self, numb):
        return np.ones((numb, numb), np.uint8)
    
    def weiguang(self):
        
        RIGHT_LOC = (1027, 1622)
        LEFT_LOC = (46, 1609)
        while True:
            if self.finish_judge():
                break
            if not exists(Template(r"tpl1628739487070.png", threshold=0.8500000000000001, record_pos=(0.005, 0.771), resolution=(1080, 1920))):
                print("撤回道具消失，进入伟光发球")
                self.get_app_img()
                try:
                    if self.get_location_node(1)[0][0] < 540:
                        sleep(2)
                        touch(RIGHT_LOC, duration=2)
                    else:
                        sleep(2)
                        touch(LEFT_LOC, duration=2)
                except:
                    pass
                else:
                    if exists(Template(r"tpl1626855250121.png",
                     record_pos=(-0.006, -0.463),
                     resolution=(1080, 1920))):
                        touch((527, 1416))
                        sleep(1)
                        touch((527, 1416))

    def run_level_main(self):
        # 第一关
        self.level_start()
        if self.level_enter_judge():
            touch((41, 972), duration=2)
            self.weiguang()
            self.level_finish()
            # self.is_gameActivity_top()
            sleep(5)
        else:
            return "关卡1，进入失败"
        # 2
        self.level_start(
            "yes",
            Template(r"tpl1626854804508.png",
                     record_pos=(0.004, -0.527),
                     resolution=(1080, 1920)), "判断是否弹出炸弹引导遮罩层")
        if self.level_enter_judge():
            touch((969, 1246), duration=2)
            self.weiguang()
            self.level_finish(10)
            # self.is_gameActivity_top()
            sleep(5)
        else:
            return "关卡2，进入失败"

        # 3
        self.level_start(
            "yes",
            Template(r"tpl1626855250121.png",
                     record_pos=(-0.006, -0.463),
                     resolution=(1080, 1920)), "判断激光砖块tips引导遮罩层")
        if self.level_enter_judge():
            touch((540, 493), duration=2)
            self.weiguang()
            self.level_finish()
            # self.is_gameActivity_top()
            sleep(5)
        else:
            return "关卡3，进入失败"
        # 4
        self.level_start()
        if self.level_enter_judge():
            touch((1017, 1208), duration=2)
            sleep(5)
            touch((1021, 1242), duration=2)
            self.level_finish(15)
            # self.is_gameActivity_top()
            sleep(5)
        else:
            return "关卡4，进入失败"

#         reward引导
        touch((590, 275))
        sleep(2)
        touch((870, 999))
        sleep(1)
        touch((341, 497))
        sleep(2)
        touch((541, 1831))
        sleep(1)
        touch((975, 246))
        sleep(1)
        touch((101,100))
        sleep(1)
        touch(Template(r"close.png",record_pos=(0.361, -0.617),resolution=(1080, 1920)))
        sleep(1)

        # 5
        self.level_start(
            "yes",
            Template(r"tpl1626854804508.png",
                     record_pos=(0.004, -0.527),
                     resolution=(1080, 1920)), "判断气泡砖块引导遮罩层")
        if self.level_enter_judge():
            touch((103, 1153), duration=2)
            self.weiguang()
            self.level_finish()
            # self.is_gameActivity_top()
            sleep(6)
        else:
            return "关卡5， 进入失败"

        # 6
        self.level_start(
            "yes",
            Template(r"tpl1626855250121.png",
                     record_pos=(-0.006, -0.463),
                     resolution=(1080, 1920)), "判断分岔砖块引导tips")
        if self.level_enter_judge():
            touch((542, 434), duration=2)
            self.weiguang()
            self.level_finish()
            # self.is_gameActivity_top()
            sleep(8)
        else:
            return "关卡6， 进入失败"

        # 7
        self.level_start()
        if self.level_enter_judge():
            touch((1013, 1183), duration=2)
            self.weiguang()
            self.level_finish(15)
            # self.is_gameActivity_top()
            sleep(5)
        else:
            return "关卡7， 进入失败"

        # 8
        self.level_start(
            "yes",
            Template(r"tpl1626854804508.png",
                     record_pos=(0.004, -0.527),
                     resolution=(1080, 1920)), "判断炸弹消除砖块引导遮罩层")
        if self.level_enter_judge():
            touch((60, 1170), duration=2)
            self.weiguang()
            self.level_finish(8)
            # self.is_gameActivity_top()
            sleep(5)
        else:
            return "关卡8， 进入失败"

        # 9
        self.level_start(
            "yes",
            Template(r"tpl1626859508189.png",
                     record_pos=(0.002, -0.544),
                     resolution=(1080, 1920)), "判断新道具引导遮罩层")
        touch((140, 1800))
        sleep(2)
        touch((536, 828))
        sleep(2)
        if self.level_enter_judge():
            touch((537, 748), duration=2)
            self.weiguang()
            self.level_finish(8)
            # self.is_gameActivity_top()
            sleep(5)
        else:
            return "关卡9， 进入失败"

        touch(
            Template(r"close.png",
                     record_pos=(0.361, -0.617),
                     resolution=(1080, 1920)))

        # 10

        self.level_start()
        if self.level_enter_judge():
            touch((1020, 948), duration=2)
            self.weiguang()
            self.level_finish(15)
            # self.is_gameActivity_top()
            sleep(5)
        else:
            return "关卡10， 进入失败"
        
        # reward
        touch((590, 275))
        sleep(2)
#         touch((870, 999))
#         sleep(1)
#         touch((341, 497))
#         sleep(2)
#         touch((541, 1831))
#         sleep(1)
#         touch((975, 246))
#         sleep(1)
#         touch((101,100))
#         sleep(1)
        touch(Template(r"close.png",record_pos=(0.361, -0.617),resolution=(1080, 1920)))
        sleep(1)

        # 11
        self.level_start(
            "yes",
            Template(r"tpl1626859508189.png",
                     record_pos=(0.002, -0.544),
                     resolution=(1080, 1920)), "判断新道具引导遮罩层")
        touch((400, 1800))
        sleep(3)
        touch((530, 1260))
        sleep(3)
        if self.level_enter_judge():
            touch((400, 1800))
            sleep(2)
            touch((542, 804))
            self.level_finish()
            # self.is_gameActivity_top()
            sleep(5)
        else:
            return "关卡11， 进入失败"

        # 12
        self.level_start()
        if self.level_enter_judge():
            touch((1024, 856), duration=2)
            self.weiguang()
            self.level_finish(10)
            # self.is_gameActivity_top()
            sleep(5)
        else:
            return "关卡12， 进入失败"

        # 13
        self.level_start(
            "yes",
            Template(r"tpl1626859508189.png",
                     record_pos=(0.002, -0.544),
                     resolution=(1080, 1920)), "判断新道具引导遮罩层")
        touch((670, 1800))
        sleep(3)
        if self.level_enter_judge():
            touch((101, 1063), duration=2)
            self.weiguang()
            self.level_finish(8)
            # self.is_gameActivity_top()
            sleep(8)
        else:
            return "关卡13， 进入失败"

        # 评论引导弹窗
        if exists(
                Template(r"tpl1626926086185.png",
                         record_pos=(0.019, -0.269),
                         resolution=(1080, 1920))):
            assert_exists(
                Template(r"tpl1626926086185.png",
                         record_pos=(0.019, -0.269),
                         resolution=(1080, 1920)), "评论引导弹窗弹出")
            touch(
                Template(r"tpl1626926276626.png",
                         record_pos=(0.018, 0.355),
                         resolution=(1080, 1920)))
            sleep(3)
            act_name = self.dev.get_top_activity_name()
            assert_equal(
                act_name,
                "com.android.vending/com.google.android.finsky.activities.MainActivity",
                "评论跳出成功检测")
            sleep(2)
            keyevent("KEYCODE_BACK")

        # 14
        self.level_start()
        if self.level_enter_judge():
            touch((400, 1800))
            sleep(2)
            touch((540, 994))
            self.level_finish(5)
            # self.is_gameActivity_top()
            sleep(5)
        else:
            return "关卡14， 进入失败"

        # 判断活动奖励
        if str(datetime.now().isoweekday()) == "4":
            assert_exists(
                Template(r"tpl1626336292054.png",
                         record_pos=(0.003, -0.535),
                         resolution=(1080, 1920)), "周4活动奖励弹出检测")
            touch(
                Template(r"claim.png",
                         record_pos=(-0.004, 0.457),
                         resolution=(1080, 1920)))
            sleep(2)
        elif str(datetime.now().isoweekday()) == "1":
            assert_exists(
                Template(r"tpl1626675233284.png",
                         record_pos=(-0.002, -0.531),
                         resolution=(1080, 1920)), "周一活动奖励弹出检测")
            touch(
                Template(r"claim.png",
                         record_pos=(-0.004, 0.457),
                         resolution=(1080, 1920)))
            sleep(2)

        # 15
        self.level_start(
            "yes",
            Template(r"tpl1626854804508.png",
                     record_pos=(0.004, -0.527),
                     resolution=(1080, 1920)), "判断木板砖块引导遮罩层")
        if self.level_enter_judge():
            touch((400, 1800))
            sleep(2)
            touch((264, 546))
            self.level_finish(8)
            self.is_gameActivity_top()
            sleep(5)
        else:
            return "关卡15， 进入失败"

        # 16
        self.level_start(
            "yes",
            Template(r"tpl1626859508189.png",
                     record_pos=(0.002, -0.544),
                     resolution=(1080, 1920)), "判断新道具引导遮罩层")
        if self.level_enter_judge():
            if not finish_judge():
                touch((972, 1744))
                sleep(0.5)
            self.level_finish()
            self.is_gameActivity_top()
            sleep(5)
        else:
            return "关卡16， 进入失败"

        # 17
        assert_exists(
            Template(r"tpl1626944729862.png",
                     record_pos=(-0.005, -0.716),
                     resolution=(1080, 1920)), "判断新手礼包弹出")

        touch(
            Template(r"close.png",
                     record_pos=(0.361, -0.617),
                     resolution=(1080, 1920)))

#         self.level_start()
#         if self.level_enter_judge():
#             touch((540, 865), duration=2)
#             self.level_finish(15)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡17， 进入失败"
        
#         # reward
#         touch((590, 275))
#         sleep(2)
#         touch((777, 324))
#         sleep(1)
# #         touch((341, 497))
# #         sleep(2)
# #         touch((541, 1831))
# #         sleep(1)
# #         touch((975, 246))
# #         sleep(1)
# #         touch((101,100))
# #         sleep(1)
#         touch(Template(r"close.png",record_pos=(0.361, -0.617),resolution=(1080, 1920)))
#         sleep(1)
        

#         # 18
#         self.level_start()
#         if self.level_enter_judge():
#             touch((105, 1075), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡18， 进入失败"

#         # 19
#         self.level_start()
#         if self.level_enter_judge():
#             sleep(2)
#             touch((200, 995), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡19， 进入失败"

#         # 20
# #         assert_exists(
# #             Template(r"tpl1626945766046.png",
# #                      record_pos=(0.015, -0.469),
# #                      resolution=(1080, 1920)), "判断小猪银行弹窗")
# #         touch(
# #             Template(r"close.png",
# #                      record_pos=(0.361, -0.617),
# #                      resolution=(1080, 1920)))
#         self.level_start()
#         if self.level_enter_judge():
#             sleep(2)
#             touch((60, 1070), duration=2)
#             self.level_finish(20)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡20， 进入失败"

#         # 21
#         self.level_start(
#             "yes",
#             Template(r"tpl1626854804508.png",
#                      record_pos=(0.004, -0.527),
#                      resolution=(1080, 1920)), "判断可乐砖块遮罩层", 5)
#         if self.level_enter_judge():
#             touch((60, 1053), duration=2)
#             self.level_finish(15)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡21， 进入失败"

#         # 22
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((50, 1062), duration=2)
#             self.level_finish(15)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡22， 进入失败"
        
#         if str(datetime.now().isoweekday()) == "3":
#             try:
#                 assert_exists(Template(r"tpl1626254570274.png", record_pos=(0.006, -0.537), resolution=(1080, 1920)), "存在周三活动完成判断")
#                 touch(Template(r"claim.png",record_pos=(-0.004, 0.457),resolution=(1080, 1920)))
#             except:
#                 print("周三活动未弹出")

#         # 23
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((93, 780), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡23， 进入失败"
        
#         if str(datetime.now().isoweekday()) == "3":
#             try:
#                 assert_exists(Template(r"tpl1626254570274.png", record_pos=(0.006, -0.537), resolution=(1080, 1920)), "存在周三活动完成判断")
#                 touch(Template(r"claim.png",record_pos=(-0.004, 0.457),resolution=(1080, 1920)))
#             except:
#                 print("周三活动未弹出")
            

#         # 24
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((135, 1134), duration=2)
#             self.level_finish(15)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡24， 进入失败"

#         # 25
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((72, 989), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡25， 进入失败"

#         # 26
#         self.level_start(
#             "yes",
#             Template(r"tpl1626854804508.png",
#                      record_pos=(0.004, -0.527),
#                      resolution=(1080, 1920)), "判断开关砖块引导遮罩层", 5)
#         if self.level_enter_judge():
#             touch((39, 1088), duration=2)
#             self.level_finish(8)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡26， 进入失败"

#         # 27
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((974, 1114), duration=2)
#             self.level_finish(5)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡27， 进入失败"

#         # 28
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((74, 1022), duration=2)
#             self.level_finish(8)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡28， 进入失败"

#         # 29
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((103, 1129), duration=2)
#             self.level_finish(5)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡29， 进入失败"

#         # 30
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((107, 1190), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡30， 进入失败"

#         # 31
#         self.level_start("yes",
#                          Template(r"tpl1626854804508.png",
#                                   record_pos=(0.004, -0.527),
#                                   resolution=(1080, 1920)),
#                          "判断云朵砖块引导遮罩层",
#                          timeout=5)
#         if self.level_enter_judge():
#             touch((974, 1223), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡31， 进入失败"

#         # 32
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((194, 1020), duration=2)
#             self.level_finish(5)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡32， 进入失败"

#         # 33
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((528, 1037), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡33， 进入失败"

#         # 34
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((821, 1186), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡34， 进入失败"
        
#         if str(datetime.now().isoweekday()) == "2":
#             try:
#                 assert_exists(Template(r"tpl1626753732349.png", record_pos=(0.0, -0.527), resolution=(1080, 1920)), "存在周二活动完成判断")
#                 touch(Template(r"claim.png",record_pos=(-0.004, 0.457),resolution=(1080, 1920)))
#             except:
#                 print("周二活动未弹出")

#         # 35
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((80, 972), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡35， 进入失败"
#         assert_exists(
#             Template(r"tpl1627021202319.png",
#                      record_pos=(0.002, -0.702),
#                      resolution=(1080, 1920)), "VIP弹出框验证")
#         touch(
#             Template(r"close.png",
#                      record_pos=(0.361, -0.617),
#                      resolution=(1080, 1920)))

#         # 36
#         self.level_start("yes",
#                          Template(r"tpl1626855250121.png",
#                                   record_pos=(-0.006, -0.463),
#                                   resolution=(1080, 1920)),
#                          "判断炮台砖块tips",
#                          timeout=5)
#         if self.level_enter_judge():
#             touch((541, 633), duration=2)
#             self.level_finish(8)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡36， 进入失败"

#         # 37
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((192, 1127), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡37， 进入失败"

#         # 38
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((85, 1153), duration=2)
#             self.level_finish(5)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡38， 进入失败"

#         # 39
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((1026, 1036), duration=2)
#             self.level_finish(8)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡39， 进入失败"

#         # 40
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((41, 968), duration=2)
#             self.level_finish(8)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡40， 进入失败"

#         # 41
#         self.level_start("yes",
#                          Template(r"tpl1626854804508.png",
#                                   record_pos=(0.004, -0.527),
#                                   resolution=(1080, 1920)),
#                          "判断小熊砖块引导遮罩层",
#                          timeout=5)
#         if self.level_enter_judge():
#             touch((987, 1064), duration=2)
#             self.level_finish(8)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡41， 进入失败"

#         # 42
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((839, 801), duration=2)
#             self.level_finish(8)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡42， 进入失败"

#         # 43
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((1016, 1129), duration=2)
#             self.level_finish(15)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡43， 进入失败"

#         # 44
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((537, 472), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡44， 进入失败"

#         # 45
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((76, 1013), duration=2)
#             self.level_finish(5)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡45， 进入失败"

#         # 46
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((50, 1090), duration=2)
#             self.level_finish(8)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡46， 进入失败"

#         # 47
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((54, 902), duration=2)
#             self.level_finish(8)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡47， 进入失败"

#         # 48
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((52, 1105), duration=2)
#             self.level_finish(8)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡48， 进入失败"

#         # 49
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((87, 981), duration=2)
#             self.level_finish(8)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡49， 进入失败"

#         # 50
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((548, 1051), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡50， 进入失败"

#         # 51
#         self.level_start("yes",
#                          Template(r"tpl1626854804508.png",
#                                   record_pos=(0.004, -0.527),
#                                   resolution=(1080, 1920)),
#                          "判断气球砖块引导遮罩层",
#                          timeout=5)
#         if self.level_enter_judge():
#             touch((104, 1208), duration=2)
#             self.level_finish(8)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡51， 进入失败"
        
#         if str(datetime.now().isoweekday()) == "2":
#             try:
#                 assert_exists(Template(r"tpl1626753732349.png", record_pos=(0.0, -0.527), resolution=(1080, 1920)), "存在周二活动完成判断")
#                 touch(Template(r"claim.png",record_pos=(-0.004, 0.457),resolution=(1080, 1920)))
#             except:
#                 print("周二活动未弹出")
        

#         # 52
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((104, 968), duration=2)
#             self.level_finish(8)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡52， 进入失败"

#         # 53
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((694, 1086), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡53， 进入失败"

#         # 54
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((100, 1112), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡54， 进入失败"

#         # 55
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((74, 1070), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡55， 进入失败"

#         # 56
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((974, 1210), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡56， 进入失败"

#         # 57
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((539, 767), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡57， 进入失败"

#         # 58
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((93, 919), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡58， 进入失败"

#         # 59
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((657, 799), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡59， 进入失败"
        
#         try:

#             assert_exists(
#                 Template(r"tpl1627027568019.png",
#                          record_pos=(0.004, -0.559),
#                          resolution=(1080, 1920)), "判断活动弹窗")
#             touch(
#                 Template(r"close.png",
#                          record_pos=(0.361, -0.617),
#                          resolution=(1080, 1920)))
#         except:
#             print("活动未开启")
            
#         try:

#             assert_exists(Template(r"tpl1627358894129.png", record_pos=(-0.006, -0.58), resolution=(1080, 1920)), "判断汽车活动开启")

#             touch(
#                 Template(r"close.png",
#                          record_pos=(0.361, -0.617),
#                          resolution=(1080, 1920)))
#         except:
#             print("汽车活动未开启")
        
#         try:
#             assert_exists(Template(r"tpl1627540068435.png", record_pos=(0.004, -0.533), resolution=(1080, 1920)), "判断仙人掌活动开启")
#             touch(
#                 Template(r"close.png",
#                          record_pos=(0.361, -0.617),
#                          resolution=(1080, 1920)))
#         except:
#             print("仙人掌活动未开启")

            

#         # 60
#         self.level_start(timeout=5)
#         if self.level_enter_judge():
#             touch((360, 826), duration=2)
#             self.level_finish(10)
#             self.is_gameActivity_top()
#             sleep(5)
#         else:
#             return "关卡60， 进入失败"


levelfinish = LevelFinish("com.brick.breaker.ball.shooting.blast")


