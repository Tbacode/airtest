'''
 * @Descripttion : 
 * @Author       : Tommy
 * @Date         : 2021-08-09 15:43:00
LastEditors: Please set LastEditors
LastEditTime: 2021-08-10 11:56:23
'''

import cv2
import os
import numpy as np
from airtest.core.api import *

# import time


class RGB2Location(object):
    
    def touch_init(self):
        sleep(2)
        touch((544, 813))
        sleep(2)
        touch((977, 1390))
        sleep(2)
    
    def get_app_img(self):
        os.system(r"adb shell screencap -p /sdcard/screen_air.jpg")
        self.push_img2devices()
    def push_img2devices(self):
        os.system(r"adb pull /sdcard/screen_air.jpg C:/Users/xt875/Documents/airtest/Color_airtest.air/screen_air.jpg")

    def set_kernel(self, numb):
        return np.ones((numb, numb), np.uint8)
    
    def difference_node(self, node_list_4, node_list_2):
        return list(set(node_list_2).difference(set(node_list_4)))
    
    def crop_img(self):
        print("进入裁剪")
        Img = cv2.imread(r"C:/Users/xt875/Documents/airtest/Color_airtest.air/screen_air.jpg")
        cropped = Img[0:1300, 0:1080] # 裁剪坐标为[y0:y1, x0:x1]
        cv2.imwrite("C:/Users/xt875/Documents/airtest/Color_airtest.air/screen_air_crop.jpg", cropped)
#         return "C:/Users/xt875/Documents/airtest/Color_airtest.air/screen_air_crop.jpg"

    def get_location_node(self, numb):
        self.crop_img()
        Img = cv2.imread("C:/Users/xt875/Documents/airtest/Color_airtest.air/screen_air_crop.jpg")  #读入一幅图像
        

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

        Lower = np.array([120, 5, 201])  #要识别颜色的下限

        Upper = np.array([120, 17, 215])  #要识别的颜色的上限

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
    
    def hint_color(self):
        # 覆盖vip购买后，使用hint道具填色的逻辑实现
        # 点击hint
        print("点击hint")
        touch((989, 102))
        sleep(3)
        touch((542, 813))
        sleep(3)
        touch((970, 1393))
        sleep(3)
        
    def run_main(self):
        if exists(Template(r"tpl1628584509786.png", record_pos=(0.143, -0.789), resolution=(1080, 1920))):
            sleep(2)

            self.get_app_img()
            node_list_4 = self.get_location_node(2)
            if node_list_4:
                print("进入卷积核2")
                for i in node_list_4:
                    touch(i)
            else:
                self.hint_color()
#                 sleep(1)
            self.get_app_img()
            node_list_2 = self.get_location_node(1)
            if node_list_2:
                print("进入卷积核1")
                diff_nodes = self.difference_node(node_list_4, node_list_2)
                for i in node_list_2:
                    touch(i)
            else:
                self.hint_color()
#                 sleep(1)
                self.run_main()
        if exists(Template(r"tpl1628835509233.png", record_pos=(-0.007, 0.638), resolution=(1080, 1920))):
            sleep(2)
            touch(Template(r"tpl1628835509233.png", record_pos=(-0.007, 0.638), resolution=(1080, 1920)))
            sleep(3)
        else:
            self.run_main()


        

