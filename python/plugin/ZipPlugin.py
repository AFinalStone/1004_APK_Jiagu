import os
import zipfile


class ZipPlugin:

    @staticmethod
    def make_zip_dir_files(source_dir, output_filename=None):
        """
        压缩指定文件夹
        :param source_dir:
        :param output_filename:
        :return:
        """
        if output_filename is None:
            output_filename = source_dir + '.zip'
        zip_file = zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(source_dir):
            for f in files:
                filename = os.path.join(root, f)
                zipfilename = filename.replace(source_dir + "\\", "")
                zip_file.write(filename, zipfilename)
        zip_file.close()

    @staticmethod
    def make_zip(source_file, output_filename):
        """
        压缩指定文件
        :param source_file:
        :param output_filename:
        :return:
        """
        if output_filename is None:
            output_filename = source_file + '.zip'
        zip_file = zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED)
        zip_file.write(source_file)
        zip_file.close()

    # @staticmethod
    # def make_file_to_zip(file, file_name, zip_file_name):
    #     """
    #     压缩指定文件到zip中
    #     :param file: 目标文件夹绝对路径
    #     :param zip_file_name
    #     :param origin_zip
    #     :return: 无
    #     """
    #     zip_file = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
    #     zip_file.write(file, file_name)
    #     zip_file.close()

    @staticmethod
    def un_zip_file(filename, output_dir):
        """
        解压zip文件
        :param filename:
        :param output_dir:
        :return:
        """
        z_file = zipfile.ZipFile(filename, "r")
        for fileM in z_file.namelist():
            z_file.extract(fileM, output_dir)
        z_file.close()

    # @staticmethod
    # def un_zip_file(filename, target_file, output_dir):
    #     z_file = zipfile.ZipFile(filename, "r")
    #     for fileM in z_file.namelist():
    #         print(fileM)
    #         # z_file.extract(fileM, output_dir)
    #     z_file.close()
