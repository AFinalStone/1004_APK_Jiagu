import os

from Crypto import Random
from Crypto.Cipher import AES


class AESPlugin:
    key = ''
    iv = ''

    def __init__(self, key, iv):
        self.key = key
        self.iv = iv

    def encrypt_str(self, data, password):
        bs = AES.block_size
        pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
        iv = Random.new().read(bs)
        cipher = AES.new(password, AES.MODE_CBC, iv)
        data = cipher.encrypt(pad(data))
        data = iv + data
        return (data)

    def decrypt_str(self, data, password):
        bs = AES.block_size
        if len(data) <= bs:
            return (data)
        unpad = lambda s: s[0:-ord(s[-1])]
        iv = data[:bs]
        cipher = AES.new(password, AES.MODE_CBC, iv)
        data = unpad(cipher.decrypt(data[bs:]))
        return (data)

    # 待加密文本补齐到 block size 的整数倍
    def padding(self, bytes):
        while len(bytes) % AES.block_size != 0:  # 循环直到补齐 AES_BLOCK_SIZE 的倍数
            bytes += ' '.encode()  # 通过补空格（不影响源文件的可读）来补齐
        return bytes  # 返回补齐后的字节列表

    # 待加密文本补齐到 block size 的整数倍
    def un_padding(self, bytes):
        while len(bytes) % AES.block_size != 0:  # 循环直到补齐 AES_BLOCK_SIZE 的倍数
            bytes -= ' '.encode()  # 通过补空格（不影响源文件的可读）来补齐
        return bytes  # 返回补齐后的字节列表

    # 加密函数
    def encrypt_byte(self, bytes):
        # 填充数据
        bytes = self.padding(bytes)
        cryptor = AES.new(str.encode(self.key), AES.MODE_CBC, str.encode(self.iv))
        ciphertext = cryptor.encrypt(bytes)
        return ciphertext

    # 解密函数
    def decrypt_byte(self, bytes):
        cryptor = AES.new(str.encode(self.key), AES.MODE_CBC, str.encode(self.iv))
        cipherbyte = cryptor.decrypt(bytes)
        # 去除填充数据
        cipherbyte = self.un_padding(cipherbyte)
        return cipherbyte

    # 加密文件
    def encrypt_byte_by_jar(self, file, encrypt_file):
        cmd = f'java -jar lib\\encrypt_tool.jar {file} {encrypt_file} {self.key} {self.iv}'
        if os.system(cmd) == 0:
            print("文件加密成功")
        else:
            print("文件加密失败")
    #
    # def decrypt_byte_by_java(self, file, encrypt_file):
    #     cmd = f'java -jar lib\\encrypt_tool.jar {file} {encrypt_file} {self.key} {self.iv}'
    #     if os.system(cmd) == 0:
    #         print("文件加密成功")
    #     else:
    #         raise Exception("文件加密失败")
