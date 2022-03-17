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
                print("old_dir=" + old_dir)
                new_dir = old_dir.replace(old_name, new_name)
                print("new_dir=" + new_dir)
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
                        print(result)
                        fileWrite.write(result)  # replace是替换，write是写入
                    fileRead.close()
                    fileWrite.close()  # 关闭文件
