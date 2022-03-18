import os

from lxml import etree

from python.plugin.AESPlugin import AESPlugin
from python.plugin.FilePlugin import FilePlugin


# 加固
class JGApplication:

    # @staticmethod
    # def change_apk_manifest_app(apk_file_name, output_file, proxy_application_name=None):
    #     """
    #     修改apk中的manifest文件，并导出
    #     :param apk_file_name:
    #     :param output_file:
    #     :param proxy_application_name:
    #     :return:
    #     """
    #     apk = APK(apk_file_name)
    #     android_manifest_axml = apk.get_android_manifest_axml()
    #     ele_root = android_manifest_axml.get_xml_obj()
    #     # 获取原始app的数据，修改xml内容
    #     ele_application = ele_root.find('application')
    #     application_name = ele_application.attrib.get("{http://schemas.android.com/apk/res/android}name")
    #     apk_package = apk.get_package()
    #     app_version_name = apk.get_androidversion_name()
    #     if proxy_application_name is None:
    #         proxy_application_name = "com.proxymder.core.ProxyApplication"
    #     element_key_name = '{http://schemas.android.com/apk/res/android}name'
    #     element_key_value = '{http://schemas.android.com/apk/res/android}value'
    #     ele_application.set(element_key_name, proxy_application_name)
    #     etree.SubElement(ele_application, _tag='meta-data',
    #                      attrib={element_key_name: 'app_name', element_key_value: application_name})
    #     etree.SubElement(ele_application, _tag='meta-data',
    #                      attrib={element_key_name: 'app_version', element_key_value: app_version_name})
    #     etree.SubElement(ele_application, _tag='meta-data',
    #                      attrib={element_key_name: 'app_package', element_key_value: apk_package})
    #     axml_byte_buffer = etree.tostring(ele_root, pretty_print=True, encoding="utf-8")
    #     FilePlugin.wirte_byte_to_file(axml_byte_buffer, output_file)

    @staticmethod
    def change_apk_manifest_txt(android_manifest_file, proxy_application_name=None, apk_package=None,
                                app_version_name=None, output_file=None):
        """
        修改manifest.xml文件
        :param android_manifest_file:
        :param proxy_application_name:
        :param apk_package:
        :param app_version_name:
        :param output_file:
        :return:
        """
        if output_file is None:
            output_file = android_manifest_file
        ele_root = etree.parse(android_manifest_file)
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

    @staticmethod
    def encrypt_dex(path, key, key_iv):
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

    # @staticmethod
    # def change_apk_dex_by_java(apk_file_name, proxy_app_aar, new_apk_file_name=None):
    #     """
    #     加密dex文件为xed文件
    #     :param proxy_app_aar:
    #     :param apk_file_name:
    #     :param new_apk_file_name:
    #     :return:
    #     """
    #     if new_apk_file_name is None:
    #         new_apk_file_name = apk_file_name.replace(".apk", "_01.apk")
    #     app_name, apk_package, app_version_name = APKPlugin.get_apk_info(apk_file_name)
    #     package_middle = apk_package.split(".")[1]
    #     # old_package = "proxycore"
    #     # new_package = "proxy" + package_middle
    #     # HookModulePlugin.change_hook_app_package(old_package, new_package)
    #     # HookModulePlugin.make_proxy_core_app()
    #     # HookModulePlugin.change_hook_app_package(new_package, old_package)
    #     # proxy_app_aar = "HookApplication/Proxy_Core/build/outputs/aar/Proxy_Core-release.aar"
    #     cmd_aes_dex = f'java -jar lib\\apk_proxy_tools.jar {apk_file_name} {proxy_app_aar} {package_middle} {new_apk_file_name}'
    #     if os.system(cmd_aes_dex) == 0:
    #         print("dex文件加密成功")
    #     else:
    #         print("dex文件加密失败")
