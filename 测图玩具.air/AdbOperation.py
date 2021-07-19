'''
 * @Descripttion : 1
 * @Author       : Tommy
 * @Date         : 2020-11-26 19:38:48
 * @LastEditors  : Tommy
 * @LastEditTime : 2020-11-26 19:57:29
'''
import subprocess
import os


class AdbOperation():
    # 封装adb 命令，返回结果为行数据
    def run_cmd(self, cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        return [i.decode() for i in p.communicate()[0].splitlines()]

    # adb 安装

    def install(self, iPath, packagename):
        tag = os.popen(
            "adb install -r {}\\{}".format(iPath, packagename)).read()
        return tag

    # adb 查询版本信息

    def inquiry_info(self, packagename):
        tag = os.popen(
            'adb shell pm dump {} | findstr "version"'.format(packagename)).read()
        return tag

    # adb 获取当前聚焦进程

    def isRunningAppActivity(self):
        tag = os.popen(
            'adb shell dumpsys activity activities | findstr "mResumedActivity"').read()
        return tag

    # adb 启动apk

    def start_apk(self, packagename, launch_activity):
        tag = os.popen("adb shell am start -n %s" %
                       (packagename + "/" + launch_activity))
        return tag
    
    # adb 将app置于后台
    def set_app_backup(self):
        os.popen("adb shell input keyevent key 3")
        
    # adb 唤醒app从后台到前台
    def app_wakeup(self, packagename, launch_activity):
        os.popen("adb shell am start -W {}".format(packagename + "/" + launch_activity))
        
