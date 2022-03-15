from python.plugin.FilePlugin import FilePlugin

content = FilePlugin.read_byte_from_file("AndroidManifest.xml")
name = content.decode('utf-8')
print(name)