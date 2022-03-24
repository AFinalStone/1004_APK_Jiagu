from python.MJBApplicationV2 import MJBApplicationV2
from python.plugin.FilePlugin import FilePlugin
from python.utils.CacheUtil import CacheUtil

if __name__ == '__main__':
    cache_util = CacheUtil("majiabao_apk_info", "main_majiabao.ini")
    # cache_util.save_value_to_cache("signature_content","--ks-key-alias yeyan --ks-pass pass:yeyan123 --key-pass  pass:yeyan123")
    # cache_util.save_value_to_cache("signature_file","签名文件.jks")
    # cache_util.save_value_to_cache("app_logo","app_logo")
    # cache_util.save_value_to_cache("new_app_logo","new_app_logo")
    # cache_util.save_value_to_cache("new_app_name","花间直播")
    # cache_util.save_value_to_cache("config_file_name","马甲包.txt")
    apk_file_name = cache_util.read_value_from_cache("apk_file_name")
    signature_file = cache_util.read_value_from_cache("signature_file")
    signature_content = cache_util.read_value_from_cache("signature_content")
    app_logo = cache_util.read_value_from_cache("app_logo")
    config_file_name = cache_util.read_value_from_cache("config_file_name")
    print("1.请确认配置了 jdk环境变量")
    print(f"2.当前配置的底包apk文件为 {apk_file_name}")
    print(f"3.当前配置的签名文件为 {signature_file}")
    print(f"3.当前配置的签名信息为 {signature_content}")
    print(f"4.当前配置的底包apk的logo文件名为 {app_logo}")
    print(f"5.当前马甲包配置信息文件为 {config_file_name}")
    input("输入任意内容以便开始任务")
    file_content = FilePlugin.read_str_from_file(config_file_name)
    app_info_list = file_content.split("\n")
    mjb = MJBApplicationV2(apk_file_name, app_logo, signature_file, signature_content)
    mjb.create_majiabao_list_apk(app_info_list)
