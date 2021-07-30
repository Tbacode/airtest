import os
from posixpath import basename
import subprocess
import requests
import shutil
import zipfile
import sys

class AirtestPython(object):
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

    def report_zip(self):
        start_dir = r'/Users/talefun/Documents/BBBAirtest/report/BBB_airtest.log/static'
        file_news = start_dir + '.zip'
        z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
        for dirpath, dirname, filenames in os.walk(start_dir):
            fpath = dirpath.replace(r'/Users/talefun/Documents/BBBAirtest/report/BBB_airtest.log', '')
            fpath = fpath and fpath + os.sep or ''
            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
                print("压缩成功")
        z.close()
    
    def report_zip_append(self):
        zip_dir = r'/Users/talefun/Documents/BBBAirtest/report/BBB_airtest.log/static.zip'
        file_news = r'/Users/talefun/Documents/BBBAirtest/report/BBB_airtest.log/log.html'
        file_news2 = r'/Users/talefun/Documents/BBBAirtest/report/BBB_airtest.log/log'
        z = zipfile.ZipFile(zip_dir, 'a', zipfile.ZIP_DEFLATED)
        for dirpath, dirname, filenames in os.walk(file_news2):
            fpath = dirpath.replace(r'/Users/talefun/Documents/BBBAirtest/report/BBB_airtest.log', '')
            
            fpath = fpath and fpath + os.sep or ''
            
            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
                print("追加压缩成功")
        basename = os.path.basename(file_news)
        z.write(file_news, basename, zipfile.ZIP_DEFLATED)
        z.close()
    
    def post_file(self, wx_url):

        headers = {"Content-Type": "text/plain"}
        data = {
            "msgtype": "text",
            "text": {
                "content": "http://192.168.2.54/BBB_airlog/static.zip"
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
        result = self.is_success(r'/Users/talefun/Documents/BBBAirtest/log/log.txt')
        if result == 1:
            self.run_sys_command(cmd2)
        return result

    def moveFile(self, target_path, source_path):
        shutil.move(source_path, target_path)


    def run_report(self,wx_url):
        self.report_zip()
        self.report_zip_append()
        self.moveFile(r'/Library/WebServer/Documents/BBB_airlog/static.zip', r'/Users/talefun/Documents/BBBAirtest/report/BBB_airtest.log/static.zip')
        res = self.post_file(wx_url)
        if res.status_code == 200:
            log_path = r'/Users/talefun/Documents/BBBAirtest/log'
            report_path = r'/Users/talefun/Documents/BBBAirtest/report/'
            self.del_log_file(log_path)
            self.del_log_file(report_path)



if __name__ == "__main__":
    ap = AirtestPython()
    cmd1 = r'python3 -m airtest run "/Users/talefun/Documents/BBBAirtest/BBB_airtest.air" --device Android://127.0.0.1:5037/HT7941A04009?cap_method=JAVACAP --log "/Users/talefun/Documents/BBBAirtest/log"'
    cmd2 = r'python3 -m airtest report "/Users/talefun/Documents/BBBAirtest/BBB_airtest.air" --log_root "/Users/talefun/Documents/BBBAirtest/log" --export "/Users/talefun/Documents/BBBAirtest/report" --lang zh'
    # id_url = r'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=eef716ba-a7e2-423e-9c9a-7cac807e397c&type=file'
    wx_url = r'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=eef716ba-a7e2-423e-9c9a-7cac807e397c'
    # file = r'/Users/talefun/Documents/BBBAirtest/report/BBB_airtest.log/static.zip'
    res = ap.run_main(cmd1, cmd2)
    if res == 1:
        ap.run_report(wx_url)
    sys.exit(res)
