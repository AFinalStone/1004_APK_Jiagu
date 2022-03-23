import os

from python.plugin.APKPlugin import APKPlugin


def change_dex_to_jar(dex_file, jar_file=None):
    """
    把dex转化成jar
    :param dex_file:
    :param jar_file:
    :return:
    """
    if dex_file is None:
        jar_file = dex_file.replace(".dex", ".jar")
    cmd = f'..\\dex2jar-2.0\\d2j-dex2jar.bat  --output {jar_file} {dex_file}'
    if os.system(cmd) == 0:
        print("成功把dex文件转化为jar文件")
    else:
        raise Exception("dex文件转化失败")


def change_jar_to_dex(jar_file, dex_file=None):
    """
    把jar转化成dex
    :param jar_file:
    :param dex_file:
    :return:
    """
    if dex_file is None:
        dex_file = jar_file.replace(".jar", ".dex")
    # cmd = f'jar2dex\\dx.bat --dex --output {dex_file} {jar_file}'
    cmd = f'dx --dex --output {dex_file} {jar_file}'
    if os.system(cmd) == 0:
        print("成功把jar文件转化为dex文件")
    else:
        raise Exception("jar文件转化为dex文件失败")


if __name__ == '__main__':
    change_jar_to_dex("..\\file_input\\classes_to_dex.jar", "..\\file_output\\classes_to_dex.dex")
    change_dex_to_jar("..\\file_input\\classes_to_jar.dex", "..\\file_output\\classes_to_jar.jar")
