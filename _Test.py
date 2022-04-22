from python.plugin.AESPlugin import AESPlugin

name = "test"

# 加解密Axml文件
# APKPlugin.decode_amxl(f"{name}/AndroidManifest.xml", f"{name}/AndroidManifest_decode.xml")
# APKPlugin.encode_amxl(f"{name}/AndroidManifest_decode.xml", f"{name}/AndroidManifest.xml")

# 使用AES算法加解密文件
# path = "file_input/app-mixin-release_res.zip"
# AESPlugin("1234567890123456", "1234567890123456").encrypt_byte_by_jar(path, path.replace(".zip", ".piz"))
path02 = "file_output/app-mixin-release_res.piz"
AESPlugin("1234567890123456", "1234567890123456").decrypt_byte_by_java(path02, path02.replace(".piz", ".zip"))

# APKPlugin.encode_amxl(f"{name}/AndroidManifest_decode.xml", f"{name}/AndroidManifest.xml")

# ZipPlugin.update_file_dir_change_time(name)
# ZipPlugin.un_zip_file(f"{name}.apk", name)
# ZipPlugin.make_zip_dir(name, f"{name}.zip")
# APKPlugin.signer_apk_file("AAAA.jks", "--ks-key-alias yeyan --ks-pass pass:yeyan123 --key-pass  pass:yeyan123 --min-sdk-version 21",
#                           f"{name}.zip", f"{name}_signer.apk")
