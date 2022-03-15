import os
import zipfile


def zipDir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹绝对路径
    :param outFullName: 压缩文件绝对路径+filename.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
    for path, _, fileList in os.walk(dirpath):
        relativePath = path.replace(dirpath, '')
        for filename in fileList:
            zip.write(os.path.join(path, filename),
                      os.path.join(relativePath, filename))
            # filename: files being zipped. arcname: filenames in zip file.
    zip.close()


path = r'米心直播'  # 字符串前加r，此时末尾不可以加\，如果要加可以加\\

folderList = os.listdir(path)

for folder in folderList:
    if path[-1] == '\\':
        dirpath = path + folder
    else:
        dirpath = path + '\\' + folder
    outFullName = dirpath + '.zip'
    zipDir(dirpath, outFullName)
