import os
import re
from threading import Thread

from python.plugin.APKPlugin import APKPlugin
from python.plugin.FilePlugin import FilePlugin


# 基准包
class JZBApplication(Thread):

    def __init__(self, apk_name, signer_file, apk_dir=None):
        self.apk_name = apk_name
        self.signer_file = signer_file
        if apk_dir is None:
            self.apk_dir = apk_name.replace(".apk", "")

    # 创建基准包
    def create_jizhunbao_apk(self, new_apk_name):
        if not os.path.isfile(self.apk_name):
            print("没有在当前目录找到AAAA.apk文件")
            return
        if not os.path.isfile(self.signer_file):
            print("没有在当前目录找到AAAA.jks签名文件")
            return
        if len(new_apk_name) == 0:
            print("新的应用名称不能为空")
            return
        try:
            APKPlugin.unzip_apk_file(self.apk_name, self.apk_dir)
            self.__change_app_name(new_apk_name)
            APKPlugin.zip_and_signer_apk_file(self.signer_file, self.apk_dir, new_apk_name + ".apk")
        except Exception as err:
            # 可能是缺少JDK或者jar包
            print(str(err) + "，可能是缺少JDK或者Jar包")

    # 批量创建基准包
    def create_jizhunbao_list_apk(self, new_apk_name_list):
        if not os.path.isfile(self.apk_name):
            print("没有在当前目录找到AAAA.apk文件")
            return
        if not os.path.isfile(self.signer_file):
            print("没有在当前目录找到AAAA.jks签名文件")
            return
        if len(new_apk_name_list) == 0:
            print("基准包名称列表不能为空")
            return
        for new_apk_name in new_apk_name_list:
            print("准备生成的基准包名称为:" + new_apk_name)
            self.create_jizhunbao_apk(new_apk_name)

    # 修改软件名称
    def __change_app_name(self, new_name="奇乐直播"):
        for root, dirs, files in os.walk(self.apk_dir):
            for file in files:
                file_path = os.path.join(root, file)  # 原来的文件路径
                if file == "strings.xml":
                    content = FilePlugin.read_str_from_file(file_path)
                    content = re.sub('<string name="app_name">.*</string>',
                                     f'<string name="app_name">{new_name}</string>',
                                     content)
                    FilePlugin.wirte_str_to_file(content, file_path)
                    break
        print("成功修改软件名称")

    # 修改软件logo
    def __change_app_logo(self, new_logo_path):
        logo_file_path = None
        for root, dirs, files in os.walk(self.apk_dir):
            for file_name in files:
                if file_name == self.apk_logo_name:
                    file_path = os.path.join(root, file_name)  # 原来的文件路径
                    logo_file_path = file_path
                    break
        if logo_file_path == None:
            print("软件logo修改失败")
        else:
            os.remove(logo_file_path)
            FilePlugin.copyfile(new_logo_path, logo_file_path)
            print("成功修改软件logo")
