import os
import time
import zipfile


class ZipPlugin:

    @staticmethod
    def make_zip_dir(source_dir, zip_file_path=None, contain_root=False):
        """
        压缩指定文件夹
        :param source_dir:
        :param zip_file_path:
        :param contain_root:
        :return:
        """
        if zip_file_path is None:
            zip_file_path = source_dir + '.zip'
        zip_file = zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(source_dir):
            for f in files:
                filename = os.path.join(root, f)
                # if contain_root is False:
                zip_file_name = filename.replace(source_dir + "\\", "")
                zip_file.write(filename, zip_file_name, compress_type=zipfile.ZIP_DEFLATED)
        zip_file.close()

    @staticmethod
    def make_zip_file(source_file, zip_file_path=None):
        """
        压缩指定文件
        :param source_file:
        :param zip_file_path:
        :return:
        """
        if zip_file_path is None:
            zip_file_path = source_file + '.zip'
        zip_file = zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED)
        zip_file.write(source_file)
        zip_file.close()

    @staticmethod
    def add_file_into_zip(target_file, target_file_path, zip_file_path):
        """
        添加特定文件到zip文件中
        :param target_file:
        :param target_file_path:
        :param zip_file_path:
        :return:
        """
        zip_file = zipfile.ZipFile(zip_file_path, "a", compression=zipfile.ZIP_DEFLATED)
        zip_file.write(target_file, arcname=target_file_path)
        zip_file.close()

    @staticmethod
    def un_zip_file(zip_file_path, output_dir):
        """
          解压zip文件
          :param zip_file_path:
          :param output_dir:
          :return:
          """
        z_file = zipfile.ZipFile(zip_file_path, "r", compression=zipfile.ZIP_DEFLATED)
        for fileM in z_file.namelist():
            z_file.extract(fileM, output_dir)
        z_file.close()

    @staticmethod
    def un_zip_target_file(zip_file_path, target_file_path, output_file_path=None):
        """
        解压zip文件中特定的文件
        :param zip_file_path:
        :param target_file_path:
        :param output_file_path:
        :return:
        """
        if output_file_path is None:
            output_file_path = zip_file_path
        z_file = zipfile.ZipFile(zip_file_path, "r", compression=zipfile.ZIP_DEFLATED)
        with z_file.open(target_file_path) as target_file:
            with open(output_file_path, "wb") as fh:
                fh.write(target_file.read())
            fh.close()
        z_file.close()

    # 修改文件的【修改日期】
    @staticmethod
    def update_file_change_time(filename, updatetime='now', access_time='now'):
        filename = os.path.abspath(filename)
        if updatetime == 'now':
            new_updatetime = time.time()
        else:
            new_updatetime = time.mktime(time.strptime(updatetime, "%Y-%m-%d %H:%M:%S"))
        if access_time == 'now':
            new_access_time = time.time()
        else:
            new_access_time = time.mktime(time.strptime(access_time, "%Y-%m-%d %H:%M:%S"))
        os.utime(filename, (new_access_time, new_updatetime))

    # 修改一个文件夹内所有文件的【修改日期】
    @staticmethod
    def update_file_dir_change_time(path):
        for i in os.listdir(path):
            file = os.path.realpath(os.path.join(path, i))
            if os.path.isfile(file):
                ZipPlugin.update_file_change_time(file)
            elif os.path.isdir(file):
                ZipPlugin.update_file_dir_change_time(file)
