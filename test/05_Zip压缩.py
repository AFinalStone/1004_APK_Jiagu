import os
import zipfile


class ZipPlugin:

    @staticmethod
    def make_zip_dir(source_dir, zip_file_path=None):
        """
        压缩指定文件夹
        :param source_dir:
        :param zip_file_path:
        :return:
        """
        if zip_file_path is None:
            zip_file_path = source_dir + '.zip'
        zip_file = zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(source_dir):
            for f in files:
                filename = os.path.join(root, f)
                zip_file_name = filename.replace(source_dir + "\\", "")
                zip_file.write(filename, zip_file_name)
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


file = "AndroidManifest_parse.xml"
file_name_in_zip = "aaa/AndroidManifest_parse_.xml"
# file_name_in_zip = "AndroidManifest.xml"
zip_file = "米心直播.zip"
ZipPlugin.add_file_into_zip("bbb.xml", "ccc/dd.xml", zip_file)
# un_zip_target_file(zip_file, file_name_in_zip, "bbb.xml")
