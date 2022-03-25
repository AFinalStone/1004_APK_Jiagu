import os

from lxml import etree

from python.plugin.APKPlugin import APKPlugin
from python.plugin.FilePlugin import FilePlugin
from python.plugin.ZipPlugin import ZipPlugin


class MJBApplicationV2:

    def __init__(self, apk_file_name, app_logo_name, signer_file, signer_content, change_axml=True):
        self.apk_file_name = apk_file_name
        self.app_logo_name = app_logo_name
        self.signer_file = signer_file
        self.signer_content = signer_content
        self.axml_arsc_decode_path = None
        self.app_logo_path_in_apk = None
        self.change_axml = change_axml
        self.apk_dir = apk_file_name.replace(".apk", "")
        self.apk_temp = apk_file_name.replace(".apk", ".zip")

    def create_majiabao_apk_by_add_arsc(self, new_app_name=None, new_app_logo=None):
        """
        此方法，修改的app_name，app名称长度不可变
        直接给apk文件追加axml文件、再签名;
        :param new_app_name:
        :param new_app_logo:
        :return:
        """
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
            new_apk_name = new_app_name + ".apk"
            self.__init_arsc_and_logo()
            # 修改axml中的app_name，并重新加密
            old_apk_name = self.apk_file_name.replace(".apk", "")
            arsc_encode_path = "resources_encode.arsc"
            APKPlugin.change_arsc_content(self.axml_arsc_decode_path, old_apk_name, new_app_name, arsc_encode_path)
            print(f"开始打包{new_apk_name}...")
            new_apk_temp = new_app_name + "_temp.apk"
            FilePlugin.copy_file(self.apk_temp, new_apk_temp)
            ZipPlugin.add_file_into_zip(arsc_encode_path, "resources.arsc", new_apk_temp)
            ZipPlugin.add_file_into_zip(new_app_logo, self.app_logo_path_in_apk, new_apk_temp)
            APKPlugin.signer_apk_file(self.signer_file, self.signer_content, new_apk_temp, new_apk_name)
            FilePlugin.remove_path_file(new_apk_temp)
            FilePlugin.remove_path_file(arsc_encode_path)
        except Exception as err:
            # 可能是缺少JDK或者jar包
            print(str(err) + "，可能是缺少JDK或者Jar包")

    def create_majiabao_apk_by_add_axml(self, new_app_name=None, new_app_logo=None):
        """
        此方法，修改的app_name，app名称长度可变
        直接给apk文件追加axml文件、再签名
        :param new_app_name:
        :param new_app_logo:
        :return:
        """
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
            new_apk_name = new_app_name + ".apk"
            self.__init_axml_and_logo()
            # 修改axml中的app_name，并重新加密
            self.__change_app_name_in_axml(self.axml_arsc_decode_path, new_app_name)
            axml_encode_path = "AndroidManifest_encode.xml"
            APKPlugin.encode_amxl(self.axml_arsc_decode_path, axml_encode_path)
            print(f"开始打包{new_apk_name}...")
            new_apk_temp = new_app_name + "_temp.apk"
            FilePlugin.copy_file(self.apk_temp, new_apk_temp)
            ZipPlugin.add_file_into_zip(axml_encode_path, "AndroidManifest.xml", new_apk_temp)
            ZipPlugin.add_file_into_zip(new_app_logo, self.app_logo_path_in_apk, new_apk_temp)
            APKPlugin.signer_apk_file(self.signer_file, self.signer_content, new_apk_temp, new_apk_name)
            FilePlugin.remove_path_file(new_apk_temp)
            FilePlugin.remove_path_file(axml_encode_path)
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
            if self.change_axml:
                self.create_majiabao_apk_by_add_axml(new_app_name, new_app_logo)
            else:
                self.create_majiabao_apk_by_add_arsc(new_app_name, new_app_logo)
        FilePlugin.remove_path_file(self.apk_temp)
        FilePlugin.remove_path_file(self.axml_arsc_decode_path)

    def __init_axml_and_logo(self):
        """
        初始化axml和logo
        :return:
        """
        if self.axml_arsc_decode_path is None:
            ZipPlugin.un_zip_file(self.apk_file_name, self.apk_dir)
            # 创建明文axml，并移除原来的axml
            axml_path = f"{self.apk_dir}/AndroidManifest.xml"
            self.axml_arsc_decode_path = "AndroidManifest_decode.xml"
            APKPlugin.decode_amxl(axml_path, self.axml_arsc_decode_path)
            APKPlugin.encode_amxl(self.axml_arsc_decode_path, axml_path)
            APKPlugin.decode_amxl(axml_path, self.axml_arsc_decode_path)
            FilePlugin.remove_path_file(axml_path)
            # 获取当前app的logo文件路径，并移除该文件
            for root, dirs, files in os.walk(self.apk_dir):
                for file_name in files:
                    if file_name == self.app_logo_name:
                        file_path = os.path.join(root, file_name)  # 原来的文件路径
                        self.app_logo_path_in_apk = file_path
                        break
            print("当前应用logo的相对位置= " + self.app_logo_path_in_apk)
            FilePlugin.remove_path_file(self.app_logo_path_in_apk)
            self.app_logo_path_in_apk = self.app_logo_path_in_apk.replace(self.apk_dir + "\\", "")
            ZipPlugin.make_zip_dir(self.apk_dir, self.apk_temp)
            FilePlugin.remove_path_file(self.apk_dir)

    def __init_arsc_and_logo(self):
        """
        初始化resource和logo
        :return:
        """
        if self.axml_arsc_decode_path is None:
            ZipPlugin.un_zip_file(self.apk_file_name, self.apk_dir)
            # 创建明文axml，并移除原来的axml
            axml_arsc_path = f"{self.apk_dir}/resources.arsc"
            self.axml_arsc_decode_path = "resources_decode.arsc"
            FilePlugin.copy_file_by_hex(axml_arsc_path, self.axml_arsc_decode_path)
            FilePlugin.remove_path_file(axml_arsc_path)
            # 获取当前app的logo文件路径，并移除该文件
            for root, dirs, files in os.walk(self.apk_dir):
                for file_name in files:
                    if file_name == self.app_logo_name:
                        file_path = os.path.join(root, file_name)  # 原来的文件路径
                        self.app_logo_path_in_apk = file_path
                        break
            print("当前应用logo的相对位置= " + self.app_logo_path_in_apk)
            FilePlugin.remove_path_file(self.app_logo_path_in_apk)
            self.app_logo_path_in_apk = self.app_logo_path_in_apk.replace(self.apk_dir + "\\", "")
            ZipPlugin.make_zip_dir(self.apk_dir, self.apk_temp)
            FilePlugin.remove_path_file(self.apk_dir)

    def __change_app_name_in_axml(self, axml_path, new_name="奇乐直播"):
        """
        修改axml中的app名称
        :param new_name:
        :return:
        """
        ele_root = etree.parse(axml_path, etree.XMLParser(encoding="utf-8"))
        ele_application = ele_root.find("application")
        if new_name is None:
            print("新应用名称不能为空")
            return
        element_key_label = '{http://schemas.android.com/apk/res/android}label'
        ele_application.set(element_key_label, new_name)
        axml_header = b'<?xml version="1.0" encoding="utf-8"?>'
        axml_body = etree.tostring(ele_root, pretty_print=True, encoding="utf-8")
        axml_byte_buffer = axml_header + axml_body
        FilePlugin.wirte_byte_to_file(axml_byte_buffer, self.axml_arsc_decode_path)
        print("成功修改软件名称")
