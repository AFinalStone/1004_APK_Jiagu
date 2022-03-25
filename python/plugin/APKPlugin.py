import os
import xml.dom.minidom
from binascii import a2b_hex


class APKPlugin:

    @staticmethod
    def unzip_apk_file(apk_file_name, output_dir=None):
        """
        解压ak文件到指定目录
        :param apk_file_name:
        :param output_dir:
        :return:
        """
        if output_dir is None:
            output_dir = apk_file_name.replace(".apk", "")
        if not os.path.exists(output_dir):
            print("开始反编译原apk...")
            cmd = f'java -jar lib\\apk_tool.jar d {apk_file_name} -o {output_dir}'
            if os.system(cmd) == 0:
                print("成功反编译原apk")
            else:
                raise Exception("反编译原apk失败")

    @staticmethod
    def zip_apk_file(apk_file_dir, apk_file=None):
        """
        把apk_file_dir文件夹打包成apk
        :param signer_file:
        :param apk_file_dir:
        :param apk_file:
        :return:
        """
        if apk_file is None:
            apk_file = apk_file_dir + ".apk"
        print("开始打包新的apk...")
        cmd_zip = f'java -jar lib\\apk_tool.jar b {apk_file_dir} -o {apk_file}'
        if os.system(cmd_zip) == 0:
            print("成功打包新的apk")
        else:
            raise Exception("打包新的apk失败")

    @staticmethod
    def signer_apk_file(signer_file, signer_content, apk_file, signer_apk_file=None):
        """
        为apk签名
        :param signer_file:
        :param signer_content:
        :param apk_file:
        :param signer_apk_file:
        :return:
        """
        if signer_apk_file is None:
            signer_apk_file = apk_file.replace(".apk", "_signer.apk")
        print("开始为apk签名...")
        cmd_signer = f'java -jar lib\\apk_signer.jar sign  --ks {signer_file} {signer_content} --out {signer_apk_file} {apk_file}'
        if os.system(cmd_signer) == 0:
            print("成功为apk签名")
        else:
            raise Exception("apk签名失败")
        os.remove(signer_apk_file + ".idsig")

    @staticmethod
    def change_dex_to_jar(dex_file, jar_file=None):
        """
        把dex转化成jar
        :param dex_file:
        :param jar_file:
        :return:
        """
        if dex_file is None:
            jar_file = dex_file.replace(".dex", ".jar")
        cmd = f'dex2jar-2.0\\d2j-dex2jar.bat  --output {jar_file} {dex_file}'
        if os.system(cmd) == 0:
            print("成功把dex文件转化为jar文件")
        else:
            raise Exception("dex文件转化失败")

    @staticmethod
    def change_jar_to_dex(jar_file, dex_file=None):
        """
        把jar转化成dex
        此方法需要配置本地的环境变量，把Android_SDK\build-tools\28.0.3目录路径添加到环境变量中
        :param jar_file:
        :param dex_file:
        :return:
        """
        if dex_file is None:
            dex_file = jar_file.replace(".jar", ".dex")
        # cmd = f'jar2dex\\dx.bat --dex --output {dex_file} {jar_file}'
        cmd = f'dx --dex --output {dex_file} {jar_file}'
        if os.system(cmd) == 0:
            print("成功把jar文件转化为dex文件")
        else:
            raise Exception("jar文件转化为dex文件失败")

    @staticmethod
    def change_arsc_content(arsc_file, old_content, new_content, new_arsc_file=None):
        """
         修改resource.arsc文件
        """
        if new_arsc_file is None:
            new_arsc_file = arsc_file.replace(".arsc", "_new.arsc")
        try:
            fr = open(arsc_file, 'rb')
            content = fr.read()
            fr.close()
            hex_content = content.hex()
            target_hex = old_content.encode("UTF-8").hex()
            hex_content = hex_content.replace(target_hex, new_content.encode("UTF-8").hex())
            hex_content = a2b_hex(hex_content)
            fw = open(new_arsc_file, 'wb')
            fw.write(hex_content)
            fw.close();
        except Exception as e:
            print(e.args)

    @staticmethod
    def decode_amxl(axml_file, par_file=None):
        """
        解析 android_manifest_file
        :param axml_file:
        :param par_file:
        :return:
        """
        if par_file is None:
            par_file = axml_file.replace(".xml", "_new.xml")
        cmd = f'java -jar lib\\xml2axml.jar d {axml_file} {par_file}'
        if os.system(cmd) == 0:
            print("成功解析axml文件")
        else:
            raise Exception("axml文件解析失败") @ staticmethod

    @staticmethod
    def encode_amxl(axml_file, par_file=None):
        """
        加密 android_manifest_file
        :param axml_file:
        :param par_file:
        :return:
        """
        if par_file is None:
            par_file = axml_file.replace(".xml", "_new.xml")
        cmd = f'java -jar lib\\xml2axml.jar e {axml_file} {par_file}'
        if os.system(cmd) == 0:
            print("成功加密axml文件")
        else:
            raise Exception("axml文件加密失败")

    @staticmethod
    def get_apk_info(android_manifest_file):
        """
        获取原始apk的信息
        :param android_manifest_file:
        :return:
        """
        # 使用minidom解析器打开 XML 文档
        DOMTree = xml.dom.minidom.parse(android_manifest_file)
        document_element = DOMTree.documentElement
        apk_package = document_element.getAttribute("package")
        app_version_name = document_element.getAttribute("android:versionName")
        ele_application = document_element.getElementsByTagName("application")[0]
        app_name = ele_application.getAttribute("android:name")
        return app_name, apk_package, app_version_name
