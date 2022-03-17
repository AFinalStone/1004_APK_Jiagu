import os


# from androguard.core.bytecodes.apk import APK


class APKPlugin(object):

    # 解压ak文件到指定目录
    @staticmethod
    def unzip_apk_file(apk_file_name, output_dir=None):
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
    def zip_and_signer_apk_file(signer_file, apk_file_dir, apk_file=None):
        """
        把apk_file_dir文件夹打包成apk
        :param signer_file:
        :param apk_file_dir:
        :param apk_file:
        :return:
        """
        if apk_file is None:
            apk_file = apk_file_dir + ".apk"
        if os.path.exists(apk_file_dir):
            print("开始打包新的apk...")
            apk_temp_name = apk_file.replace(".apk", "_temp.apk")
            cmd_zip = f'java -jar lib\\apk_tool.jar b {apk_file_dir} -o {apk_temp_name}'
            if os.system(cmd_zip) == 0:
                print("成功打包新的apk")
            else:
                raise Exception("打包新的apk失败")
            print("开始为新的apk签名...")
            cmd_signer = f'java -jar lib\\apk_signer.jar sign  --ks {signer_file} --ks-key-alias yeyan --ks-pass pass:yeyan123 --key-pass  pass:yeyan123 --out {apk_file} {apk_temp_name}'
            if os.system(cmd_signer) == 0:
                print("成功打包新的apk")
            else:
                raise Exception("为新的apk签名失败")
            os.remove(apk_temp_name)
            os.remove(apk_file + ".idsig")

            print("成功为新的apk签名")

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
        cmd = f'dex2jar-2.0/d2j-dex2jar.bat  --output {dex_file} {jar_file}'
        if os.system(cmd) == 0:
            print("成功把dex文件转化为jar文件")
        else:
            raise Exception("dex文件转化失败")

    @staticmethod
    def change_jar_to_dex(jar_file, dex_file=None):
        """
        把jar转化成dex
        :param jar_file:
        :param dex_file:
        :return:
        """
        if dex_file is None:
            dex_file = jar_file.replace(".jar", ".dex")
        cmd = f'dx --dex --output {jar_file} {dex_file}'
        if os.system(cmd) == 0:
            print("成功把jar文件转化为dex文件")
        else:
            raise Exception("jar文件转化失败")

    @staticmethod
    def get_apk_info(apk_file_name):
        """
        获取原始apk的信息
        :param apk_file_name:
        :return:
        """
        app_name = "com.example.shellapplication.MIApplication"
        apk_package = "com.example.shellapplication"
        app_version_name = "1.0.0"
        return app_name, apk_package, app_version_name

    # @staticmethod
    # def get_apk_info(apk_file_name):
    #     """
    #     获取原始apk的信息
    #     :param apk_file_name:
    #     :return:
    #     """
    #     apk = APK(apk_file_name)
    #     app_name = apk.get_app_name()
    #     apk_package = apk.get_package()
    #     app_version_name = apk.get_androidversion_name()
    #     return app_name, apk_package, app_version_name
