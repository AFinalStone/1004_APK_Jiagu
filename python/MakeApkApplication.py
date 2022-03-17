# 加固
import os
import re

from python.plugin.GitPlugin import GitPlugin


class MakeApkApplication(object):

    @staticmethod
    def createLocalPropertiesFile(sourceDir, fileName, root_sdk_dir):
        if not os.path.exists(sourceDir):
            return
        fileDir = sourceDir + '/' + fileName
        if os.path.exists(fileDir):
            return
        f = open(fileDir, 'w')
        f.write('sdk.dir=' + root_sdk_dir)
        f.close()

    @staticmethod
    def makeApk(git_clone_address, target_branch, sdk_path, gradle_path="gradle", gradle_task=None):
        pattern = re.compile('[a-zA-Z0-9]/[a-zA-Z0-9]*.git')  # 查找数字
        code_dir_list = pattern.search(git_clone_address).group()
        code_dir = code_dir_list.replace(".git", "").replace("/", "")[1:]
        print(code_dir)
        if os.path.exists(code_dir) is False:
            GitPlugin.git_clone(git_clone_address)
        MakeApkApplication.createLocalPropertiesFile(code_dir, 'local.properties', sdk_path)
        origin_cwd = os.getcwd()
        os.chdir(code_dir)
        GitPlugin.git_check(target_branch)
        if gradle_task is None:
            gradle_task = "app:assembleRelease"
        cmd = f'{gradle_path} {gradle_task}'
        os.system(cmd)
        os.chdir(origin_cwd)
