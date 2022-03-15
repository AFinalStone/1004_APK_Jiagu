from python.JGApplication import JGApplication
from python.plugin.APKSignerPlugin import APKSignerPlugin
from python.plugin.FilePlugin import FilePlugin

if __name__ == '__main__':
    apk_name = "米心直播.apk"
    proxy_application_name = "com.proxygtzbabc.core.ProxyApplication"
    new_apk_name = "米心直播_new.apk"
    # JGApplication.change_apk_dex(apk_name, "179D278870E26DBF", "FBD62E078872D971", "米心直播_01.zip")
    APKSignerPlugin.unzip_apk_file("米心直播_01.zip", "米心直播_01")
    apk_package, app_version_name = JGApplication.get_apk_info(apk_name)
    JGApplication.change_apk_manifest_txt("米心直播_01\\AndroidManifest.xml", "米心直播_01\\AndroidManifest.xml",
                                          proxy_application_name, apk_package,
                                          app_version_name)
    APKSignerPlugin.zip_and_signer_apk_file("米心直播.jks", "米心直播_01", "米心直播_03.apk")
    # android_manifest = FilePlugin().read_str_from_file()
