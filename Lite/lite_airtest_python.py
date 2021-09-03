'''
 * @Descripttion : lite自动化调度脚本
 * @Author       : Tommy
 * @Date         : 2021-09-01 17:30:01
 * @LastEditors  : Tommy
 * @LastEditTime : 2021-09-03 14:25:23
'''
import os
import requests
import shutil
import zipfile
import sys
import time


class AirtestPython(object):
    def get_img_by_suffixes(self, path, suffixes=('png'), traverse=False):
        file_list = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file_suffix = os.path.splitext(file)[1][1:].lower()
                if file_suffix in suffixes:
                    file_list.append(file)
            if not traverse:
                return file_list
        return file_list

    def run_sys_command(self, command):
        # result = subprocess.Popen(command, stdout=subprocess.PIPE)
        # res_list =  [i.decode() for i in result.communicate()[0].splitlines()]
        # res = os.popen(command)
        os.system(command)

    def is_success(self, log_path):
        with open(log_path, 'r') as f:
            log_info = f.read()
            # print("+" * 20)
            # print(log_info)
            # print("+" * 20)
        if "OK" not in log_info:
            return 1
        else:
            return 0

    def report_zip(self, item_log):
        time_str = time.strftime("%Y%m%d%H%M%S", time.localtime())
        '''
        ---------MAC配置---------
        start_dir = r'/Users/talefun/Documents/lite_airtest/report/LITE_airtest.log/static'
        '''
        start_dir = r'C:/Users/talefun/Documents/airtest/Lite/report/{}/static'.format(
            item_log)
        file_news = start_dir + '-' + '{}.zip'.format(time_str)
        z = zipfile.ZipFile(str(file_news), 'w', zipfile.ZIP_DEFLATED)
        for dirpath, dirname, filenames in os.walk(start_dir):
            '''
            ---------MAC配置---------
            fpath = dirpath.replace(r'/Users/talefun/Documents/lite_airtest/report/LITE_airtest.log', '')
            '''
            fpath = dirpath.replace(
                r'C:\Users\talefun\Documents\airtest\Lite\report\{}'.format(item_log), '')
            fpath = fpath and fpath + os.sep or ''
            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
                print("压缩成功")
        z.close()
        '''
        ---------MAC配置---------
        return file_news.replace(r'/Users/talefun/Documents/lite_airtest/report/LITE_airtest.log/static', '')
        '''
        return file_news.replace(start_dir, '')

    def report_zip_append(self, file_news, item_log):
        '''
        ---------MAC配置---------
        zip_dir = r'/Users/talefun/Documents/lite_airtest/report/LITE_airtest.log/static{}'.format(file_news)
        file_log = r'/Users/talefun/Documents/lite_airtest/report/LITE_airtest.log'
        file_news = r'/Users/talefun/Documents/lite_airtest/report/LITE_airtest.log/log.html'
        file_news2 = r'/Users/talefun/Documents/lite_airtest/report/LITE_airtest.log/log'
        '''
        zip_dir = r'C:\Users\talefun\Documents\airtest\Lite\report\{}\static{}'.format(
            item_log, file_news)
        file_log = r'C:\Users\talefun\Documents\airtest\Lite\report\{}'.format(
            item_log)
        file_news = r'C:\Users\talefun\Documents\airtest\Lite\report\{}\log.html'.format(
            item_log)
        file_news2 = r'C:\Users\talefun\Documents\airtest\Lite\report\{}\log'.format(
            item_log)
        z = zipfile.ZipFile(zip_dir, 'a', zipfile.ZIP_DEFLATED)
        for dirpath, dirname, filenames in os.walk(file_news2):
            '''
            ---------MAC配置--------
            fpath = dirpath.replace(r'/Users/talefun/Documents/lite_airtest/report/LITE_airtest.log', '')
            '''
            fpath = dirpath.replace(
                r'C:\Users\talefun\Documents\airtest\Lite\report\{}'.format(item_log), '')

            fpath = fpath and fpath + os.sep or ''

            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
                print("追加压缩成功")
        basename = os.path.basename(file_news)
        z.write(file_news, basename, zipfile.ZIP_DEFLATED)
        png_list = self.get_img_by_suffixes(file_log)
        for filename in png_list:
            z.write(os.path.join(file_log, filename), filename)
        z.close()

    def post_file(self, wx_url, file_news, item_air):

        headers = {"Content-Type": "text/plain"}
        data = {
            "msgtype": "text",
            "text": {
                # "content": "http://172.31.60.64/Lite_airlog/TCL{}".format(file_news) MAC配置
                "content": "http://172.31.60.64/Lite_airlog/{}-{}".format(item_air, file_news)
            }
        }

        res = requests.post(wx_url, json=data, headers=headers)

        # data = {'file': open(file, 'rb')}
        # response = requests.post(url=id_url, files=data)
        # json_res = response.json()
        # print("+" * 20)
        # print(json_res)
        # print("+" * 20)
        # media_id = json_res['media_id']

        # data = {"msgtype": "file", "file":{"media_id": media_id}}
        # result = requests.post(url=wx_url, json=data)
        return (res)

    def del_log_file(self, path):
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                shutil.rmtree(c_path, True)
            else:
                os.remove(c_path)

    def run_main(self, cmd1, cmd2):
        self.run_sys_command(cmd1)
        '''
        ---------MAC配置---------
        result = self.is_success(r'/Users/talefun/Documents/lite_airtest/log/log.txt')
        '''
        result = self.is_success(
            r'C:\Users\talefun\Documents\airtest\Lite\log\log.txt')
        if result == 1:
            self.run_sys_command(cmd2)
        return result

    def moveFile(self, target_path, source_path):
        shutil.move(source_path, target_path)

    def run_report(self, wx_url, item_log, item_air):
        file_news = self.report_zip(item_log)
        self.report_zip_append(file_news, item_log)
        '''
        ---------MAC配置---------
        self.moveFile(r'/Library/WebServer/Documents/Lite_airlog/{}-{}'.format(item_air, file_news),
                      r'/Users/talefun/Documents/lite_airtest/report/{}/static{}'.format(item_log, file_news))
        res = self.post_file(wx_url, file_news, item_air)
        if res.status_code == 200:
            log_path = r'/Users/talefun/Documents/lite_airtest/log'
            report_path = r'/Users/talefun/Documents/lite_airtest/report/'
            self.del_log_file(log_path)
            self.del_log_file(report_path)
        '''


if __name__ == "__main__":
    ap = AirtestPython()
    airproject_list = ["lite_newuser.air",
                       "lite_setting.air",
                       "lite_coloring.air"]

    for lite_item in airproject_list:
        '''
        ---------MAC配置---------
            cmd1 = r'python3 -m airtest run "/Users/talefun/Documents/lite_airtest/LITE_airtest.air" --device Android://127.0.0.1:5037/HT7941A04009 --log "/Users/talefun/Documents/lite_airtest/log"'
            cmd2 = r'python3 -m airtest report "/Users/talefun/Documents/lite_airtest/LITE_airtest.air" --log_root "/Users/talefun/Documents/lite_airtest/log" --export "/Users/talefun/Documents/lite_airtest/report" --lang zh'
        '''
        cmd1 = r'python -m airtest run "C:\Users\talefun\Documents\airtest\Lite\{}" --device Android://127.0.0.1:5037/HT7941A04009 --log "C:\Users\talefun\Documents\airtest\Lite\log"'.format(
            lite_item)
        cmd2 = r'python -m airtest report "C:\Users\talefun\Documents\airtest\Lite\{}" --log_root "C:\Users\talefun\Documents\airtest\Lite\log" --export "C:\Users\talefun\Documents\airtest\Lite\report" --lang zh'.format(
            lite_item)
    # id_url = r'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=eef716ba-a7e2-423e-9c9a-7cac807e397c&type=file'
        wx_url = r'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=eef716ba-a7e2-423e-9c9a-7cac807e397c'
        # file = r'/Users/talefun/Documents/BBBAirtest/report/BBB_airtest.log/static.zip'
        res = ap.run_main(cmd1, cmd2)
        # if res == 1:
        #     ap.run_report(wx_url)
        item_log = lite_item.replace("air", "log")
        ap.run_report(wx_url, item_log, lite_item)
        # sys.exit(res)
