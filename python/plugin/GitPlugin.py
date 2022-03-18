import os


class GitPlugin:

    @staticmethod
    def git_clone(code_address):
        cmd = f"git clone {code_address}"
        os.system(cmd)

    @staticmethod
    def git_pull():
        cmd = f"git pull"
        os.system(cmd)

    @staticmethod
    def git_check(target_branch):
        cmd = f"git checkout {target_branch}"
        os.system(cmd)
