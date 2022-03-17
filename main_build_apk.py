from python.MakeApkApplication import MakeApkApplication

if __name__ == '__main__':
    code_dir = "ShellApplication"
    # code_dir = "D:\Android_Project\MiYue\michat-master02"
    # git_clone_address = "http://giitt.yonrun.com:1323/clinet/michat.git"
    git_clone_address = "git@github.com:AFinalStone/ShellApplication.git"
    target_branch_name = "dev_1.0.0"
    MakeApkApplication.makeApk(git_clone_address, target_branch_name, r"D\:\\Android_SDK")
