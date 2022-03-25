import os

from lxml import etree

from python.plugin.AESPlugin import AESPlugin
from python.plugin.APKPlugin import APKPlugin
from python.plugin.FilePlugin import FilePlugin
# 对apk进行自定义加固操作，添加代理app，加密*.dex后缀的文件
from python.plugin.HookModulePlugin import HookModulePlugin
from python.plugin.ZipPlugin import ZipPlugin


class JGApplication:

    def __init__(self, signer_file, signer_content, ):
        self.signer_file = signer_file
        self.signer_content = signer_content

    def create_jiagu_apk_by_hook_application(self, apk_file_name, android_sdk_path=None, gradle_path=None):
        """
        创建加固apk文件，会自动根据apk本身的包名动态修改壳app的包名路径，还支持修改AES加密的key,iv
        :return:
        """
        if not os.path.isfile(apk_file_name):
            print(f"没有在当前目录找到{apk_file_name}文件")
            return
        if not os.path.isfile(self.signer_file):
            print(f"没有在当前目录找到{self.signer_file}.jks签名文件")
            return
        apk_dir = apk_file_name.replace(".apk", "")
        apk_file_xed_name = apk_file_name.replace(".apk", "_xed.apk")
        FilePlugin.remove_path_file(apk_dir)
        ZipPlugin.un_zip_file(apk_file_name, apk_dir)
        axml_file = f"{apk_dir}\\AndroidManifest.xml"
        axml_decode_file = "AndroidManifest_decode.xml"
        # 解密axl
        APKPlugin.decode_amxl(axml_file, axml_decode_file)
        APKPlugin.encode_amxl(axml_decode_file, axml_file)
        APKPlugin.decode_amxl(axml_file, axml_decode_file)
        apk_name, apk_package, app_version_name = APKPlugin.get_apk_info(axml_decode_file)
        # 获取代理自定义代理app的相关参数
        package_middle = apk_package.split(".")[1]
        package_middle = "proxy" + package_middle
        proxy_aar_file = f"{package_middle}.aar"
        proxy_application_name = f"com.{package_middle}.core.ProxyApplication"
        # 替换axml
        self.__change_apk_manifest_txt(axml_decode_file, proxy_application_name, apk_package, app_version_name)
        APKPlugin.encode_amxl(axml_decode_file, axml_file)
        FilePlugin.remove_path_file(axml_decode_file)
        # 加密dex文件，保证这里的key,iv和hookapplication//Proxy_Core模块代码里面的key,iv一致
        self.__encrypt_dex(apk_dir, "1234567890123456", "1234567890123456")
        # 修改AndroidSDK路径
        FilePlugin.wirte_str_to_file('sdk.dir=' + android_sdk_path, "HookApplication/local.properties")
        HookModulePlugin.change_core_app_package(HookModulePlugin.origin_name, package_middle)
        HookModulePlugin.make_proxy_core_app(gradle_path=gradle_path)
        HookModulePlugin.change_core_app_package(package_middle, HookModulePlugin.origin_name)
        FilePlugin.move_file("HookApplication/Proxy_Core/build/outputs/aar/Proxy_Core-release.aar", proxy_aar_file)
        ZipPlugin.un_zip_file(proxy_aar_file, "proxy_aar_temp")
        APKPlugin.change_jar_to_dex("proxy_aar_temp/classes.jar")
        FilePlugin.move_file("proxy_aar_temp/classes.dex", f"{apk_dir}/classes.dex")
        FilePlugin.remove_path_file("proxy_aar_temp")
        FilePlugin.remove_path_file(proxy_aar_file)
        ZipPlugin.make_zip_dir(apk_dir, apk_file_xed_name)
        FilePlugin.remove_path_file(apk_dir)
        # 重新签名
        APKPlugin.signer_apk_file(self.signer_file, self.signer_content, apk_file_xed_name,
                                  apk_file_xed_name.replace("_xed.apk", "_signer.apk"))
        FilePlugin.remove_path_file(apk_file_xed_name)

    def create_jiagu_apk(self, apk_file_name):
        """
        创建加固apk文件，代理app的包名路固定为com.proxycore.core.ProxyApplication
        :return:
        """
        if not os.path.isfile(apk_file_name):
            print(f"没有在当前目录找到{apk_file_name}文件")
            return
        if not os.path.isfile(self.signer_file):
            print(f"没有在当前目录找到{self.signer_file}.jks签名文件")
            return
        apk_dir = apk_file_name.replace(".apk", "")
        apk_file_xed_name = apk_file_name.replace(".apk", "_xed.apk")
        FilePlugin.remove_path_file(apk_dir)
        ZipPlugin.un_zip_file(apk_file_name, apk_dir)
        axml_file = f"{apk_dir}\\AndroidManifest.xml"
        axml_decode_file = "AndroidManifest_decode.xml"
        # 解密axl
        APKPlugin.decode_amxl(axml_file, axml_decode_file)
        APKPlugin.encode_amxl(axml_decode_file, axml_file)
        APKPlugin.decode_amxl(axml_file, axml_decode_file)
        apk_name, apk_package, app_version_name = APKPlugin.get_apk_info(axml_decode_file)
        # 获取代理自定义代理app的相关参数
        proxy_application_name = "com.proxycore.core.ProxyApplication"
        # 替换axml
        self.__change_apk_manifest_txt(axml_decode_file, proxy_application_name, apk_package, app_version_name)
        APKPlugin.encode_amxl(axml_decode_file, axml_file)
        FilePlugin.remove_path_file(axml_decode_file)
        # 加密dex文件
        self.__encrypt_dex(apk_dir, "1234567890123456", "1234567890123456")
        # 添加壳app
        FilePlugin.copy_file("lib/proxy_application.dex", f"{apk_dir}/classes.dex")
        ZipPlugin.make_zip_dir(apk_dir, apk_file_xed_name)
        FilePlugin.remove_path_file(apk_dir)
        # 重新签名
        APKPlugin.signer_apk_file(self.signer_file, self.signer_content, apk_file_xed_name,
                                  apk_file_xed_name.replace("_xed.apk", "_signer.apk"))
        FilePlugin.remove_path_file(apk_file_xed_name)

    def __change_apk_manifest_txt(self, android_manifest_file, proxy_application_name=None, apk_package=None,
                                  app_version_name=None, output_file=None):
        """
        修改manifest.xml文件中的关键字段
        :param android_manifest_file:
        :param proxy_application_name:
        :param apk_package:
        :param app_version_name:
        :param output_file:
        :return:
        """
        if output_file is None:
            output_file = android_manifest_file
        ele_root = etree.parse(android_manifest_file, etree.XMLParser(encoding="utf-8"))
        ele_application = ele_root.find("application")
        if apk_package is None or app_version_name is None or proxy_application_name is None:
            print("参数不完整")
            return
        application_name = ele_application.attrib.get("{http://schemas.android.com/apk/res/android}name")
        element_key_name = '{http://schemas.android.com/apk/res/android}name'
        element_key_value = '{http://schemas.android.com/apk/res/android}value'
        ele_application.set(element_key_name, proxy_application_name)

        etree.SubElement(ele_application, _tag='meta-data',
                         attrib={element_key_name: 'app_name', element_key_value: application_name})
        etree.SubElement(ele_application, _tag='meta-data',
                         attrib={element_key_name: 'app_version', element_key_value: app_version_name})
        etree.SubElement(ele_application, _tag='meta-data',
                         attrib={element_key_name: 'app_package', element_key_value: apk_package})
        axml_byte_buffer = etree.tostring(ele_root, pretty_print=True, encoding="utf-8")
        FilePlugin.wirte_byte_to_file(axml_byte_buffer, output_file)

    def __encrypt_dex(self, path, key, key_iv):
        """
        加密dex文件为xed文件
        :param path:
        :param key:
        :param key_iv:
        :return:
        """
        aesPlugin = AESPlugin(key, key_iv)
        if os.path.isfile(path):
            if path.find(".dex") != -1:
                aesPlugin.encrypt_byte_by_jar(path, path.replace(".dex", ".xed"))
        else:
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)  # 原来的文件路径
                    if file_path.find(".dex") != -1:
                        # bytes = FilePlugin.read_byte_from_file(file_path)
                        aesPlugin.encrypt_byte_by_jar(file_path, file_path.replace(".dex", ".xed"))
                        os.remove(file_path)
