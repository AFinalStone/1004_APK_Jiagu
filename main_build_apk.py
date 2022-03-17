from python.MakeApkApplication import MakeApkApplication
from python.utils.CacheUtil import CacheUtil

if __name__ == '__main__':
    # # git_clone_address = "http://giitt.yonrun.com:1323/clinet/michat.git"
    # git_clone_address = "https://github.com/AFinalStone/ShellApplication.git"
    # # git_clone_address = "git@github.com:AFinalStone/ShellApplication.git"
    # target_branch_name = "dev_1.0.0"
    # # # target_branch_name = "dev_2.0.23.0"
    # sdk_path = r"D\:\\Android_SDK"
    # sdk_path = r"C\:\\Users\\david\\AppData\\Local\\Android\\Sdk"
    cache_util = CacheUtil("build_apk_info")
    # cache_util.save_value_to_cache("git_clone_address", "https://github.com/AFinalStone/ShellApplication.git")
    # cache_util.save_value_to_cache("target_branch_name", "dev_1.0.0")
    # cache_util.save_value_to_cache("sdk_path", "D\:\\Android_SDK")
    # cache_util.save_value_to_cache("gradle_path", "gradle")
    # cache_util.save_value_to_cache("gradle_task", "app:assembleRelease")
    # cache_util.save_value_to_cache("source_apk", "app/qlbf/release/app-qlbf-release.apk")
    git_clone_address = cache_util.read_value_from_cache("git_clone_address")
    target_branch_name = cache_util.read_value_from_cache("target_branch_name")
    sdk_path = cache_util.read_value_from_cache("sdk_path")
    gradle_path = cache_util.read_value_from_cache("gradle_path")
    gradle_task = cache_util.read_value_from_cache("gradle_task")
    source_apk = cache_util.read_value_from_cache("source_apk")
    print(git_clone_address)
    MakeApkApplication.makeApk(git_clone_address, target_branch_name, sdk_path, source_apk=source_apk)
