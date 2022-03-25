import os
import re

from python.plugin.FilePlugin import FilePlugin
from python.plugin.GitPlugin import GitPlugin


# 对指定代码仓库分支进行下载，切换分支，自动打包的操作
class MakeApkApplication:

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
    def makeApk(git_clone_address, target_branch, sdk_path, gradle_path="gradle", gradle_task="build", source_apk=None):
        pattern = re.compile('[a-zA-Z0-9]/[a-zA-Z0-9]*.git')
        code_dir = pattern.search(git_clone_address).group()
        code_dir = code_dir.replace(".git", "").replace("/", "")[1:]
        print(code_dir)
        if os.path.exists(code_dir) is False:
            GitPlugin.git_clone(git_clone_address)
        MakeApkApplication.createLocalPropertiesFile(code_dir, 'local.properties', sdk_path)
        origin_cwd = os.getcwd()
        os.chdir(code_dir)
        GitPlugin.git_check(target_branch)
        cmd = f'{gradle_path} {gradle_task}'
        os.system(cmd)
        os.chdir(origin_cwd)
        if source_apk is None:
            source_apk = "app/build/outputs/apk/release/app-release.apk"
        source_apk = code_dir + "/" + source_apk
        FilePlugin.copy_file(source_apk, "app_release.apk")
