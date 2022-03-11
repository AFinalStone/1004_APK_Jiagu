import os
import shutil


class FilePlugin(object):
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
    def copyfile(srcfile, dstfile):
        """
        拷贝文件
        :param srcfile:
        :param dstfile:
        :return:
        """
        if not os.path.isfile(srcfile):
            print("%s not exit!" % (srcfile))
        else:
            fpath, fname = os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
            shutil.copyfile(srcfile, dstfile)
        else:
            shutil.copyfile(srcfile, dstfile)
