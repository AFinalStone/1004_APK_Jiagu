from python.plugin.APKPlugin import APKPlugin
from python.plugin.ZipPlugin import ZipPlugin

name = "app-qlbf-release"

# APKPlugin.decode_apk_by_axml_print(f"{name}/AndroidManifest.xml", f"{name}/AndroidManifest_decode.xml")
# APKPlugin.decode_apk_by_axml_print("壳工程_release/AndroidManifest.xml", "壳工程_release/AndroidManifest_decode.xml")

# APKPlugin.decode_amxl("AndroidManifest.xml", "AndroidManifest_decode.xml")
# APKPlugin.encode_amxl("AndroidManifest_decode.xml", "AndroidManifest.xml")

# ZipPlugin.update_file_dir_change_time(name)
ZipPlugin.make_zip_dir(name, f"{name}.zip")
APKPlugin.signer_apk_file("AAAA.jks", "--ks-key-alias yeyan --ks-pass pass:yeyan123 --key-pass  pass:yeyan123 ",
                          f"{name}.zip", f"{name}_signer.apk")


