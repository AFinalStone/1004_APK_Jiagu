import os
import zipfile


class ZipPlugin(object):

    # 打包目录中所有文件
    @staticmethod
    def make_zip_dir_files(source_dir, output_filename):
        if output_filename is None:
            output_filename = source_dir + '.zip'
        zip_file = zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(source_dir):
            for f in files:
                filename = os.path.join(root, f)
                zipfilename = filename.replace(source_dir + "\\", "")
                zip_file.write(filename, zipfilename)
        zip_file.close()

    # 打包目录为zip文件
    @staticmethod
    def make_zip(file, output_file):
        """
        压缩指定文件夹
        :param dirpath: 目标文件夹绝对路径
        :param outFullName: 压缩文件绝对路径+filename.zip
        :return: 无
        """
        zip_file = zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED)
        zip_file.write(file)
        zip_file.close()

    @staticmethod
    def un_zip_file(filename, output_dir):
        z_file = zipfile.ZipFile(filename, "r")
        for fileM in z_file.namelist():
            z_file.extract(fileM, output_dir)
        z_file.close()
