import os
import zipfile


class ZipPlugin(object):

    # 打包目录为zip文件（未压缩）
    @staticmethod
    def make_zip(source_dir, output_filename):
        zipf = zipfile.ZipFile(output_filename, 'w')
        pre_len = len(os.path.dirname(source_dir))
        for parent, dirnames, filenames in os.walk(source_dir):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
                zipf.write(pathfile, arcname)
        zipf.close()

    @staticmethod
    def un_zip_file(filename, output_dir):
        z_file = zipfile.ZipFile(filename, "r")
        for fileM in z_file.namelist():
            z_file.extract(fileM, output_dir)
        z_file.close()
