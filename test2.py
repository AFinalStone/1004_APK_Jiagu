from Crypto.Cipher import AES

from python.plugin.AESPlugin import AESPlugin
from python.plugin.FilePlugin import FilePlugin

AES_SECRET_KEY = ''
IV = ''


# # padding算法
# BS = 0
# pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
# unpad = lambda s: s[0:-ord(s[-1:])]


# 待加密文本补齐到 block size 的整数倍
def padding(bytes):
    while len(bytes) % AES.block_size != 0:  # 循环直到补齐 AES_BLOCK_SIZE 的倍数
        bytes += ' '.encode()  # 通过补空格（不影响源文件的可读）来补齐
    return bytes  # 返回补齐后的字节列表


# 待加密文本补齐到 block size 的整数倍
def unPadding(bytes):
    while len(bytes) % AES.block_size != 0:  # 循环直到补齐 AES_BLOCK_SIZE 的倍数
        bytes -= ' '.encode()  # 通过补空格（不影响源文件的可读）来补齐
    return bytes  # 返回补齐后的字节列表


# 加密函数
def encrypt_byte(key, byte):
    cryptor = AES.new(key.encode("utf8"), AES.MODE_CBC, IV.encode("utf8"))
    ciphertext = cryptor.encrypt(byte)
    return ciphertext


# 解密函数
def decrypt_byte(key, byte):
    cryptor = AES.new(key.encode("utf8"), AES.MODE_CBC, IV.encode("utf8"))
    cipherbyte = cryptor.decrypt(byte)
    # 去除填充
    cipherbyte = unPadding(cipherbyte)
    return cipherbyte


if __name__ == '__main__':
    # 随机生成16位字符串作为加密的key
    # AES_SECRET_KEY = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    # jks的MD5值
    MD5 = 'F8:F9:29:9B:ED:4A:FF:4E:17:9D:27:88:70:E2:6D:BF'
    md5list = MD5.split(':', 15)
    md5str = ''
    for a in md5list:
        md5str = md5str + a
    print('md5str:', md5str)
    IV = md5str[0:16]
    AES_SECRET_KEY = md5str[16:32]
    aesPlugin = AESPlugin(AES_SECRET_KEY, IV)
    # bytes = FilePlugin.read_byte_from_file("classes01.dex")
    # encrypt_content = aesPlugin.encrypt_byte(bytes)
    # FilePlugin.wirte_byte_to_file(encrypt_content, "classes02.dex")
    bytes = FilePlugin.read_byte_from_file("classes02.dex")
    decrypt_content = aesPlugin.decrypt_byte(bytes)
    FilePlugin.wirte_byte_to_file(decrypt_content, "classes03.dex")
    # print(decrypt_content)
