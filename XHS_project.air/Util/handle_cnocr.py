'''
 * @Descripttion : 
 * @Author       : Tommy
 * @Date         : 2022-05-05 17:52:32
 * @LastEditors  : Tommy
 * @LastEditTime : 2022-05-06 16:16:00
'''
import cv2
import pyocr
from PIL import Image as PI
import io
import os
from cnocr import CnOcr
import warnings
warnings.filterwarnings("ignore")



class Handle_Cnocr():

    def __init__(self) -> None:
        self.left = 800
        self.right = 150
        self.top = 3000
        self.buttom = 100
        self.save_path = r'C:\Users\talefun\Documents\airtest\XHS_project.air\images\newImg\img_release.png'
        self.targets_path = r'C:\Users\talefun\Documents\airtest\XHS_project.air\images\targets\xhs_release.jpg'
        self.ocr = CnOcr()

    def save_cropImg(self):
        '''
         * @name: Tommy
         * @msg: 根据目标地址图片，截图点赞区域图片，保存新的图片
         * @param {*} self
         * @param {*} save_path 保存地址
         * @param {*} targets_path 目标地址
         * @return {*}
        '''
        # img = cv2.imread(self.targets_path)
        with open(self.targets_path, 'rb') as fp:
            a = fp.read()

        new_img = PI.open(io.BytesIO(a))
        img_x = new_img.crop(
            (self.left, self.top, self.left+self.right, self.top+self.buttom))
        img_x.save(self.save_path)

    def get_likeNum_by_cnocr(self):
        '''
         * @name: Tommy
         * @msg: 
         * @param {*} self
         * @return {*} 返回点赞数
        '''
        img_text = self.ocr.ocr(self.save_path)
        new_no = ''
        for j in img_text:
            for m in j[0]:
                new_no += m
        print(f'点赞数为：{new_no}')
        try:
            new_no = int(new_no)
        except ValueError:
            return -999999
        return new_no

handleOcr = Handle_Cnocr()

