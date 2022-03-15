import os

code_dir = "michat-master"
# code_dir = "D:\Android_Project\MiYue\michat-master02"
# git_clone_address = "http://giitt.yonrun.com:1323/clinet/michat.git"
target_branch_name = ""

if os.path.exists(code_dir):
    os.chdir(code_dir)
    print('进入michat-master下： ' + os.getcwd())
    os.system('git pull')
    # os.system('git checkout dev_2.0.23.0')
    # os.system('gradle clean')
    os.system('gradle resguardMixinRelease')
else:
    print('code_dir不存在')
