'''
 * @Descripttion : 
 * @Author       : Tommy
 * @Date         : 2022-05-05 18:48:22
 * @LastEditors  : Tommy
 * @LastEditTime : 2022-05-06 17:34:39
'''
# -*- encoding=utf8 -*-
__author__ = "talefun"
import sys
sys.path.append(r'C:\Users\talefun\Documents\airtest\XHS_project.air')
from airtest.core.api import *
using(r'XHS_project.air')
from Util.handle_excel import excel
from Util.handle_cnocr import handleOcr

auto_setup(__file__)


def get_url_list(excel_item):
    url_list = []
    # 第一列不能为none
    if excel_item[0] is not None:
        # 判断连接不为空
        for cut_item in excel_item[2:]:
            if cut_item is not None:
                if "xiaohongshu" in cut_item:
                    url_list.append(cut_item)
                else:
                    url_list = []
    if len(url_list) != 0:
        return url_list
    else:
        return "存在其他平台或无跳转连接，不予统计"


def airtest_go(url):
#     return 56
    # 启动浏览器程序
    start_app('com.android.browser')
    sleep(8)
    touch((560, 489))
    sleep(2)
    text(url)
    sleep(5)
    touch(Template(r"tpl1651832062219.png", record_pos=(-0.006, 0.749), resolution=(1440, 3200)))

    if wait(Template(r"tpl1651824690615.png", record_pos=(0.033, 0.999), resolution=(1440, 3200))):
        snapshot(r'C:\Users\talefun\Documents\airtest\XHS_project.air\images\targets\xhs_release.jpg')
    # 关闭浏览器
    stop_app('com.android.browser')
    # 保存点赞区域图片
    handleOcr.save_cropImg()
    # 识别点赞数
    like_num = handleOcr.get_likeNum_by_cnocr()
    return like_num
       

def main():
    excel_data = excel.get_excel_data()
    for index, excel_item in enumerate(excel_data):
        # 获取可执行的url集合
        url_list = get_url_list(excel_item)
        print(url_list)
        # 判断返回值是否url
        if isinstance(url_list, list):
            write_str = ''
            like_sum = 0
            for url_index, url in enumerate(url_list):
                # 调用airtest方法，执行自动化
                like_num = airtest_go(url)
                write_str += '链接{}点赞数：{}\n'.format(url_index+1, like_num)
                like_sum += like_num
            write_str += "点赞总数：{}".format(like_sum)
            excel.excel_write_data(index + 4, 2, write_str)
        else:
            excel.excel_write_data(index + 4, 2, url_list)


if __name__ == "__main__":
    main()


