import os

from lxml import etree

from python.plugin.APKPlugin import APKPlugin
from python.plugin.FilePlugin import FilePlugin
from python.plugin.ZipPlugin import ZipPlugin


class MJBApplication:

    def __init__(self, apk_file_name, signer_file, app_logo_name, apk_dir=None):
        self.apk_file_name = apk_file_name
        self.app_logo_name = app_logo_name
        self.signer_file = signer_file
        if apk_dir is None:
            self.apk_dir = apk_file_name.replace(".apk", "")

    # 创建马甲包
    def create_majiabao_apk(self, new_app_name=None, new_app_logo=None):
        if not os.path.isfile(self.apk_file_name):
            print(f"没有在当前目录找到{self.apk_file_name}文件")
            return
        if not os.path.isfile(self.signer_file):
            print(f"没有在当前目录找到{self.signer_file}签名文件")
            return
        if (new_app_name is None or len(new_app_name) == 0) and new_app_logo is None:
            print("新的应用名和logo不能同时为空")
            return
        try:
            if not os.path.exists(self.apk_dir):
                ZipPlugin.un_zip_file(self.apk_file_name, self.apk_dir)
            self.__change_app_name_by_axml(new_app_name)
            self.__change_app_logo(new_app_logo)
            new_apk_temp_name = new_app_name + "_temp.apk"
            new_apk_name = new_app_name + ".apk"
            ZipPlugin.make_zip_dir(self.apk_dir, new_apk_temp_name)
            APKPlugin.signer_apk_file(self.signer_file, new_apk_temp_name, new_apk_name)
            FilePlugin.remove_path_file(new_apk_temp_name)
            # FilePlugin.remove_path_file(self.apk_dir)
        except Exception as err:
            # 可能是缺少JDK或者jar包
            print(str(err) + "，可能是缺少JDK或者Jar包")

    # 批量创建马甲包
    def create_majiabao_list_apk(self, new_app_info_list):
        if not os.path.isfile(self.apk_file_name):
            print(f"没有在当前目录找到{self.apk_file_name}文件")
            return
        if not os.path.isfile(self.signer_file):
            print(f"没有在当前目录找到{self.signer_file}签名文件")
            return
        if len(new_app_info_list) == 0:
            print("马甲包名称列表不能为空")
            return
        for new_app_info in new_app_info_list:
            new_app_name = new_app_info.split(",")[0]
            new_app_logo = new_app_info.split(",")[1]
            print("开始生成马甲包...")
            print("应用名称=" + new_app_name + " 应用图标=" + new_app_logo)
            self.create_majiabao_apk(new_app_name, new_app_logo)
        FilePlugin.remove_path_file(self.apk_dir)

    # 修改软件名称

    # 修改软件名称
    def __change_app_name_by_axml(self, new_name="奇乐直播"):
        axml_path = f"{self.apk_dir}/AndroidManifest.xml"
        axml_decode_path = "AndroidManifest_decode.xml"
        APKPlugin.decode_apk_by_axml_print(axml_path, axml_decode_path)
        ele_root = etree.parse(axml_decode_path, etree.XMLParser(encoding="utf-8"))
        ele_application = ele_root.find("application")
        if new_name is None:
            print("新应用名称不能为空")
            return
        element_key_label = '{http://schemas.android.com/apk/res/android}label'
        print(ele_application)
        # new_name = new_name.encode("utf-8")
        # print(chardet.detect(new_name))
        ele_application.set(element_key_label, new_name)
        axml_header = b'<?xml version="1.0" encoding="utf-8"?>'
        axml_body = etree.tostring(ele_root, pretty_print=True, encoding="utf-8")
        axml_byte_buffer = axml_header + axml_body
        FilePlugin.wirte_byte_to_file(axml_byte_buffer, axml_decode_path)
        APKPlugin.encode_amxl(axml_decode_path, axml_path)
        FilePlugin.remove_path_file(axml_decode_path)
        print("成功修改软件名称")

    # 修改软件logo
    def __change_app_logo(self, new_logo_path="logo.png"):
        logo_file_path = None
        for root, dirs, files in os.walk(self.apk_dir):
            for file_name in files:
                if file_name == self.app_logo_name:
                    file_path = os.path.join(root, file_name)  # 原来的文件路径
                    logo_file_path = file_path
                    break
        if new_logo_path is None:
            print("新应用logo不能为空")
        else:
            os.remove(logo_file_path)
            FilePlugin.copy_file(new_logo_path, logo_file_path)
            print("成功修改软件logo")
