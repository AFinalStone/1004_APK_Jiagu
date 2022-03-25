from binascii import a2b_hex

import chardet

from python.plugin.FilePlugin import FilePlugin


def test_gbk_utf_8():
    str = "中国"
    str_gbk = str.encode("GBK")
    str_gbk_hex = str_gbk.hex()
    str_utf8 = str.encode("UTF-8")
    str_utf8_hex = str_utf8.hex()
    barrs = bytearray(str, "UTF-8")

    print(str)
    print("GBK type", type(str_gbk))
    print("GBK 编码：", str_gbk)
    print("GBK Chardet：", chardet.detect(str_gbk))
    print("GBK-HEX type", type(str_gbk_hex))
    print("GBK-HEX 编码：", str_gbk_hex)

    print("UTF-8 type：", type(str_utf8))
    print("UTF-8 编码：", str_utf8)
    print("UTF-8 Chardet：", chardet.detect(str_utf8))
    print("UTF-8-HEX type", type(str_utf8_hex))
    print("UTF-8-HEX 编码：", str_utf8_hex)

    print("barrs byte 编码：", barrs)
    print("barrs type：", type(barrs))
    for utf8_item in str_utf8:
        print("byte 编码：", utf8_item)
    barrs[0] = "C".encode("UTF-8")[0]

    print("UTF-8 解码：", str_utf8.decode('UTF-8'))
    print("GBK 解码：", str_gbk.decode('GBK'))
    print("GBK-HEX 解码：", a2b_hex(str_gbk_hex))
    print("UTF-8-HEX 编码：", a2b_hex(str_utf8_hex))


# test_gbk_utf_8()
content = FilePlugin.read_byte_from_file("..\\file_input\\resources.arsc")
hex_content = content.hex()
target_hex01 = "ShellApplication".encode("UTF-8").hex()
target_hex02 = "新的名字".encode("UTF-8").hex()
hex_content = hex_content.replace(target_hex01, "ApplicationShell".encode("UTF-8").hex())
hex_content = hex_content.replace(target_hex02, "测试名称".encode("UTF-8").hex())
hex_content = a2b_hex(hex_content)
FilePlugin.wirte_byte_to_file(hex_content, "..\\file_output\\resources.arsc")
