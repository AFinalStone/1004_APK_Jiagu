from python.JGApplication import JGApplication
from python.plugin.APKPlugin import APKPlugin
from python.utils.CacheUtil import CacheUtil

if __name__ == '__main__':
    cache_util = CacheUtil("jiagu_apk_info")
    # cache_util.save_value_to_cache("apk_file_name", "奇乐直播.apk")
    # cache_util.save_value_to_cache("signature_file", "签名文件.jks")
    # cache_util.save_value_to_cache("proxy_application_name", "com.proxycore.core.ProxyApplication")
    # cache_util.save_value_to_cache("proxy_aar_file", "ProxyApplication.aar")
    apk_file_name = cache_util.read_value_from_cache("apk_file_name")
    signature_file = cache_util.read_value_from_cache("signature_file")
    proxy_application_name = cache_util.read_value_from_cache("proxy_application_name")
    proxy_aar_file = cache_util.read_value_from_cache("proxy_aar_file")

    apk_file_dir = apk_file_name.replace(".apk", "")
    APKPlugin.unzip_apk_file(apk_file_name, apk_file_dir)
    axml_file = f"{apk_file_dir}\\AndroidManifest.xml"
    apk_name, apk_package, app_version_name = APKPlugin.get_apk_info(axml_file)
    print(apk_name)
    print(apk_package)
    print(app_version_name)
    # JGApplication.change_apk_manifest_txt(axml_file, proxy_application_name, apk_package, app_version_name)

    # new_apk_file_name = apk_file_name.replace(".apk", "_shell.apk")
    # new_apk_file_dir = apk_file_name.replace(".apk", "")
    # JGApplication.change_apk_dex_by_java(apk_file_name, proxy_aar_file, new_apk_file_name)
    # APKPlugin.zip_and_signer_apk_file(signature_file, new_apk_file_dir, new_apk_file_name)
