from python.plugin.APKPlugin import APKPlugin
from python.plugin.ZipPlugin import ZipPlugin

name = "test"

APKPlugin.decode_amxl(f"{name}/AndroidManifest.xml", f"{name}/AndroidManifest_decode.xml")

# APKPlugin.encode_amxl(f"{name}/AndroidManifest_decode.xml", f"{name}/AndroidManifest.xml")

# ZipPlugin.update_file_dir_change_time(name)
# ZipPlugin.un_zip_file(f"{name}.apk", name)
# ZipPlugin.make_zip_dir(name, f"{name}.zip")
# APKPlugin.signer_apk_file("AAAA.jks", "--ks-key-alias yeyan --ks-pass pass:yeyan123 --key-pass  pass:yeyan123 --min-sdk-version 21",
#                           f"{name}.zip", f"{name}_signer.apk")
