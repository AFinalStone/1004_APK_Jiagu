import os

code_dir = "apk_code_dir"
Root_SDK_Dir = "D\:\\Android_SDK"


def createLocalPropertiesFile(sourceDir, fileName, root_sdk_dir):
    if not os.path.exists(sourceDir):
        return
    fileDir = sourceDir + '/' + fileName
    if os.path.exists(fileDir):
        return
    f = open(fileDir, 'w');
    f.write('sdk.dir=' + root_sdk_dir)
    f.close()


createLocalPropertiesFile(code_dir, 'local.properties', Root_SDK_Dir)
