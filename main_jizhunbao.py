from python.plugin.APKSignerPlugin import APKSignerPlugin
from python.plugin.FilePlugin import FilePlugin
from python.JZBApplication import JZBApplication

if __name__ == '__main__':
    apk_name = "奇乐直播.apk"
    signature_file = "奇乐直播.jks"
    print("1.请确认电脑已经安装了JDK，并配置了java环境变量")
    print("2.请确保底包文件为奇乐直播.apk，并放到当前目录下")
    print("3.请修改签名文件为奇乐直播.jks，并放到当前目录下")
    print("4.请确保配置文件为name_list.txt，并放到当前目录下")
    input("输入任意内容以便开始任务")
    content_input = FilePlugin.read_str_from_file("name_list.txt")
    jizhunbao_name_list = content_input.split("\n")
    JZBApplication(apk_name, signature_file).create_jizhunbao_list_apk(jizhunbao_name_list)
