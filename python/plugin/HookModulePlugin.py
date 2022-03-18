import os

from python.plugin.FilePlugin import FilePlugin


class HookModulePlugin:
    origin_name = "proxycore"

    @staticmethod
    def change_core_app_package(old_package, new_package):
        """
        使用代码创建app文件
        :param old_package:
        :param new_package:
        :return:
        """
        FilePlugin.replace_file_content(r"HookApplication\Proxy_Core", old_package, new_package)
        FilePlugin.replace_folder_name(r"HookApplication\Proxy_Core", old_package, new_package)

    @staticmethod
    def make_proxy_core_app(gradle_path="gradle", clean_cache=False):
        """
        使用代码创建app文件
        :param gradle_task:
        :param clean_cache:
        :return:
        """
        code_dir = r"HookApplication"
        gradle_task = ":Proxy_Core:assembleRelease"
        if os.path.exists(code_dir):
            origin_cwd = os.getcwd()
            os.chdir(code_dir)
            if clean_cache:
                print("开始清空gradle缓存...")
                cmd = f'{gradle_path} clean'
                os.system(cmd)
            if gradle_task is not None and len(gradle_task) > 0:
                cmd = f'{gradle_path} {gradle_task}'
                if os.system(cmd) == 0:
                    print("成功打包aar文件")
                else:
                    print("打包aar文件失败")
            os.chdir(origin_cwd)
        else:
            print(f'{code_dir}不存在')
