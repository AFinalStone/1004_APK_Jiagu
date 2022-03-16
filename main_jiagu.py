from python.JGApplication import JGApplication
from python.plugin.APKPlugin import APKPlugin

if __name__ == '__main__':
    apk_file_name = "奇乐直播.apk"
    signature_file = "奇乐直播.jks"
    print("1.请确认电脑已经安装了JDK，并配置了java环境变量")
    print("2.请确保底包文件为奇乐直播.apk，并放到当前目录下")
    print("3.请修改签名文件为奇乐直播.jks，并放到当前目录下")
    input("输入任意内容以便开始任务")
    new_apk_file_name = apk_file_name.replace(".apk", "_shell.apk")
    new_apk_file_dir = apk_file_name.replace(".apk", "")
    apk_name, apk_package, app_version_name = APKPlugin.get_apk_info(apk_file_name)
    proxy_application_name = "com.proxycore.core.ProxyApplication"
    JGApplication.change_apk_dex_by_java(apk_file_name, "ProxyApplication.aar", new_apk_file_name)
    APKPlugin.unzip_apk_file(new_apk_file_name, new_apk_file_dir)
    axml_file = f"{new_apk_file_dir}\\AndroidManifest.xml"
    JGApplication.change_apk_manifest_txt(axml_file, proxy_application_name, apk_package, app_version_name)
    APKPlugin.zip_and_signer_apk_file(signature_file, new_apk_file_dir, new_apk_file_name)
