import os


# 打包
class MakeApkApplication(object):

    # # 使用代码创建apk
    # @staticmethod
    # def make_apk_by_code(code_dir, gradle_task, pull_code=False, target_branch=None, clean_cache=False):
    #     if os.path.exists(code_dir):
    #         os.chdir(code_dir)
    #         print('进入michat-master下： ' + os.getcwd())
    #         if pull_code:
    #             print("开始更新代码...")
    #             cmd = 'git pull'
    #             os.system(cmd)
    #         if target_branch is not None:
    #             print("开始切换代码分支...")
    #             cmd = f'git checkout {target_branch}'
    #             os.system(cmd)
    #         if clean_cache:
    #             print("开始清空gradle缓存...")
    #             cmd = 'gradle clean'
    #             os.system(cmd)
    #         if gradle_task is not None and len(gradle_task) > 0:
    #             cmd = f'gradle {gradle_task}'
    #             if os.system(cmd) == 0:
    #                 print("成功打包apk文件")
    #             else:
    #                 raise Exception("打包apk文件失败")
    #         else:
    #             print(f"{gradle_task}参数错误")
    #     else:
    #         print('code_dir不存在')

    # 使用代码创建app文件
    @staticmethod
    def make_app_by_code(code_dir, gradle_task, clean_cache=False):
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
