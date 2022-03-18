import os

from python.plugin.FilePlugin import FilePlugin


class HookModulePlugin:

    @staticmethod
    def change_hook_app_package(old_package, new_package):
        """
        使用代码创建app文件
        :param old_package:
        :param new_package:
        :return:
        """
        FilePlugin.replace_file_content(r"HookApplication\Proxy_Guard_Core", old_package, new_package)
        FilePlugin.replace_folder_name(r"HookApplication\Proxy_Guard_Core", old_package, new_package)

    @staticmethod
    def change_tools_app_package(old_package, new_package):
        """
        使用代码创建app文件
        :param old_package:
        :param new_package:
        :return:
        """
        FilePlugin.replace_file_content(r"HookApplication\Proxy_Guard_Tools", old_package, new_package)
        FilePlugin.replace_folder_name(r"HookApplication\Proxy_Guard_Tools", old_package, new_package)

    @staticmethod
    def make_proxy_core_app(clean_cache=False):
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
                cmd = 'gradle clean'
                os.system(cmd)
            if gradle_task is not None and len(gradle_task) > 0:
                cmd = f'gradle {gradle_task}'
                if os.system(cmd) == 0:
                    print("成功打包aar文件")
                else:
                    print("打包aar文件失败")
            os.chdir(origin_cwd)
        else:
            print('code_dir不存在')

    @staticmethod
    def make_proxy_tools_app(clean_cache=False):
        """
        使用代码创建app文件
        :param clean_cache:
        :return:
        """
        code_dir = r"HookApplication"
        gradle_task = ":Proxy_Tools:build"
        if os.path.exists(code_dir):
            origin_cwd = os.getcwd()
            os.chdir(code_dir)
            if clean_cache:
                print("开始清空gradle缓存...")
                cmd = 'gradle clean'
                os.system(cmd)
            if gradle_task is not None and len(gradle_task) > 0:
                cmd = f'gradle {gradle_task}'
                if os.system(cmd) == 0:
                    print("成功打包aar文件")
                else:
                    print("打包aar文件失败")
            os.chdir(origin_cwd)
        else:
            print('code_dir不存在')
