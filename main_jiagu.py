import base64

from python.JGApplication import JGApplication
from python.plugin.AESPlugin import AESPlugin
from python.plugin.FilePlugin import FilePlugin

if __name__ == '__main__':
    # apk_name = "米心直播.apk"
    # JGApplication.change_apk_dex(apk_name)
    JGApplication.change_apk_manifest("米心直播._apk")
