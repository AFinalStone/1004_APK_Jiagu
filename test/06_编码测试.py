def test_gbk_utf_8():
    str = "小米之家"
    str_utf8 = str.encode("UTF-8")
    str_gbk = str.encode("GBK")
    print(str)
    print("UTF-8 编码：", str_utf8)
    print("GBK 编码：", str_gbk)
    print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
    print("GBK 解码：", str_gbk.decode('GBK', 'strict'))
    # UTF-8 编码： b'\xe8\x8a\xb1\xe9\x97\xb4____01'
    # GBK 编码： b'\xbb\xa8\xbc\xe4____01'


def get_resource_arsc(filename):
    """
    从文件中读取byte
    :param filename:
    :param contents:
    :return:
    """
    try:
        fh = open(filename, 'rb')
        content = fh.read()
        fh.close()
    except:
        content = None
    print(content)


print("shellApplication".encode('UTF-8'))
print("shellApplication".encode('GBK'))

get_resource_arsc("..\\file_input\\resources.arsc")
