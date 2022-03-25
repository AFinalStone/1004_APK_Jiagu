import os
import shutil
from binascii import a2b_hex


class FilePlugin:
    FILE_NAME_PATTERN = r"[\/\\\:\*\?\"\<\>\|]"

    @staticmethod
    def wirte_str_to_file(content, filename):
        """
        把字符串写入到文件中
        :param filename:
        :param content:
        :return:
        """
        # 文件夹不存在则先创建文件夹
        dir_name = os.path.dirname(filename)
        if not os.path.exists(dir_name) and len(dir_name) > 0:
            os.makedirs(dir_name)
        fh = open(filename, 'w', encoding='utf-8')
        fh.write(content)
        fh.close()

    @staticmethod
    def wirte_byte_to_file(byte_buff, filename):
        """
        把字符串写入到文件中
        :param filename:
        :param content:
        :return:
        """
        # 文件夹不存在则先创建文件夹
        dir_name = os.path.dirname(filename)
        if not os.path.exists(dir_name) and len(dir_name) > 0:
            os.makedirs(dir_name)
        with open(filename, "wb") as fh:
            fh.write(byte_buff)
        fh.close()

    @staticmethod
    def read_str_from_file(filename):
        """
        从文件中读取字符串
        :param filename:
        :param contents:
        :return:
        """
        try:
            fh = open(filename, 'r', encoding='utf-8')
            content = fh.read()
            fh.close()
        except:
            content = ""
        return content

    @staticmethod
    def read_byte_from_file(filename):
        """
        从文件中读取byte
        :param filename:
        :param contents:
        :return:
        """
        try:
            fh = open(filename, 'rb')
            content = fh.read()
            fh.close()
        except:
            content = None
        return content

    @staticmethod
    def copy_file(srcfile, dstfile):
        """
        拷贝文件
        :param srcfile:
        :param dstfile:
        :return:
        """
        if not os.path.isfile(srcfile):
            print("%s not exit!" % (srcfile))
            return
        if dstfile.find("/") == -1:
            fpath, fname = None, dstfile
        else:
            fpath, fname = os.path.split(dstfile)
        if fpath is not None and not os.path.exists(fpath):
            os.makedirs(fpath)
            shutil.copyfile(srcfile, dstfile)
        else:
            shutil.copyfile(srcfile, dstfile)

    @staticmethod
    def copy_file_by_hex(srcfile, dstfile):
        """
        拷贝文件
        :param srcfile:
        :param dstfile:
        :return:
        """
        if not os.path.isfile(srcfile):
            print("%s not exit!" % (srcfile))
            return
        if dstfile.find("/") == -1:
            fpath, fname = None, dstfile
        else:
            fpath, fname = os.path.split(dstfile)
        if fpath is not None and not os.path.exists(fpath):
            os.makedirs(fpath)
        # hexdata = "0123456789ABCDEF"  # 注意：str中的十六进制码的数量必须是偶数个，否则 a2b_hex 函数运行会出错；
        # "A~F"的大小写无所谓；
        # 除了"0~9"、"A~F"外，不要包含其他字符，例如：空格、\t
        with open(srcfile, 'rb') as frb:
            with open(dstfile, "wb") as fwb:
                hexdata = frb.read().hex()
                fwb.write(a2b_hex(hexdata))  # 把16进制字符串转化为2进制
            frb.close()
            fwb.close()

    @staticmethod
    def move_file(srcfile, dstfile):
        """
        移除文件/文件夹
        :param path:
        :return:
        """
        if not os.path.isfile(srcfile):
            print("%s not exit!" % (srcfile))
            return
        if dstfile.find("/") == -1:
            fpath, fname = None, dstfile
        else:
            fpath, fname = os.path.split(dstfile)
        if fpath is not None and not os.path.exists(fpath):
            os.makedirs(fpath)
            shutil.move(srcfile, dstfile)
        else:
            shutil.move(srcfile, dstfile)

    @staticmethod
    def replace_folder_name(filePath, old_name, new_name):
        """
        替换文件夹名称
        :param filePath:
        :param old_name:
        :param new_name:
        :return:
        """
        for root, dirs, files in os.walk(filePath):
            for dir in dirs:
                old_dir = os.path.join(root, dir)  # 原来的文件路径
                # print("old_dir=" + old_dir)
                new_dir = old_dir.replace(old_name, new_name)
                # print("new_dir=" + new_dir)
                if old_dir != new_dir:
                    os.rename(old_dir, new_dir)  # 重命名

    @staticmethod
    def replace_file_content(filePath, old_name, new_name):
        """
        替换文件内容
        :param filePath:
        :param old_name:
        :param new_name:
        :return:
        """
        for root, dirs, files in os.walk(filePath):
            for file in files:
                filename = os.path.join(root, file)
                if filename.endswith('.java') or filename.endswith('.xml') or filename.endswith(
                        '.json') or filename.endswith('.pro'):
                    fileRead = open(filename, 'r', encoding='UTF-8')
                    lines = fileRead.readlines()
                    fileWrite = open(filename, 'w', encoding='UTF-8')
                    for s in lines:
                        result = s.replace(old_name, new_name)
                        # print(result)
                        fileWrite.write(result)  # replace是替换，write是写入
                    fileRead.close()
                    fileWrite.close()  # 关闭文件

    @staticmethod
    def remove_path_file(path):
        """
        移除文件/文件夹
        :param path:
        :return:
        """
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)
