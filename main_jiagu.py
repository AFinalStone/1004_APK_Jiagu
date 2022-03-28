from python.JGApplication import JGApplication
from python.plugin.HookModulePlugin import HookModulePlugin
from python.utils.CacheUtil import CacheUtil

if __name__ == '__main__':
    # cache_util.save_value_to_cache("signature_content","--ks-key-alias yeyan --ks-pass pass:yeyan123 --key-pass  pass:yeyan123")

    cache_util = CacheUtil("jiagu_apk_info", "main_jiagu.ini")
    apk_file_name = cache_util.read_value_from_cache("apk_file_name")
    signature_file = cache_util.read_value_from_cache("signature_file")
    signature_content = cache_util.read_value_from_cache("signature_content")
    android_sdk_path = cache_util.read_value_from_cache("android_sdk_path", 'D\\:\\\\Android_SDK')
    gradle_path = cache_util.read_value_from_cache("gradle_path", "gradle")
    print("1.请确认配置了 jdk环境变量")
    print("2.请确认文件路径 没有中文")
    print(f"3.当前配置的apk文件为 {apk_file_name}")
    print(f"4.当前配置的签名文件为 {signature_file}")
    print(f"4.当前配置的签名信息为 {signature_content}")
    print(f"6.当前电脑配置的android_sdk路径为 {android_sdk_path}")
    print(f"5.当前电脑配置的gradle_path路径为 {gradle_path}")
    input("输入任意内容以便开始任务")
    jgApp = JGApplication(signer_file=signature_file, signer_content=signature_content)
    jgApp.create_jiagu_apk(apk_file_name=apk_file_name)
    # jgApp.create_jiagu_apk_by_hook_application(apk_file_name=apk_file_name,
    #                                            android_sdk_path=android_sdk_path
    #                                            , gradle_path=gradle_path)
