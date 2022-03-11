import os


class APKSignerPlugin(object):

    # 解压ak文件到指定目录
    @staticmethod
    def unzip_apk_file(apk_file_name, output_dir=None):
        if output_dir is None:
            output_dir = apk_file_name.replace(".apk", "")
        if not os.path.exists(output_dir):
            print("开始反编译原apk...")
            cmd = f'java -jar lib\\apktool.jar d {apk_file_name} -o {output_dir}'
            if os.system(cmd) == 0:
                print("成功反编译原apk")
            else:
                raise Exception("反编译原apk失败")

    # 对解压的apk文件重新打包
    @staticmethod
    def zip_and_signer_apk_file(signer_file, apk_file_dir, apk_file=None):
        if apk_file is None:
            apk_file = apk_file_dir + ".apk"
        if os.path.exists(apk_file_dir):
            print("开始打包新的apk...")
            apk_temp_name = apk_file.replace(".apk", "_temp.apk")
            cmd_zip = f'java -jar lib\\apktool.jar b {apk_file_dir} -o {apk_temp_name}'
            if os.system(cmd_zip) == 0:
                print("成功打包新的apk")
            else:
                raise Exception("打包新的apk失败")
            print("开始为新的apk签名...")
            cmd_signer = f'java -jar lib\\apksigner.jar sign  --ks {signer_file} --ks-key-alias yeyan --ks-pass pass:yeyan123 --key-pass  pass:yeyan123 --out {apk_file} {apk_temp_name}'
            if os.system(cmd_signer) == 0:
                print("成功打包新的apk")
            else:
                raise Exception("为新的apk签名失败")
            os.remove(apk_temp_name)
            os.remove(apk_file + ".idsig")

            print("成功为新的apk签名")

    @staticmethod
    def change_dex_to_jar():
        print("开始反把dex文件转化为jar文件...")
        cmd = 'dex2jar-2.0/d2j-dex2jar.bat  classes.dex'
        if os.system(cmd) == 0:
            print("成功把dex文件转化为jar文件")
        else:
            raise Exception("dex文件转化失败")

    @staticmethod
    def change_dir_to_dex():
        print("开始反把dex文件转化为jar文件...")
        cmd = 'dx --dex --output=classes.dex classes'
        if os.system(cmd) == 0:
            print("成功把dex文件转化为jar文件")
        else:
            raise Exception("dex文件转化失败")
