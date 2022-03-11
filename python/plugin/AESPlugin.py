from Crypto import Random
from Crypto.Cipher import AES


class AESPlugin(object):
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
    def encrypt_byte(self, byte):
        # 填充数据
        byte = self.padding(byte)
        cryptor = AES.new(str.encode(self.key), AES.MODE_CBC, str.encode(self.iv))
        ciphertext = cryptor.encrypt(byte)
        return ciphertext

    # 解密函数
    def decrypt_byte(self, byte):
        cryptor = AES.new(str.encode(self.key), AES.MODE_CBC, str.encode(self.iv))
        cipherbyte = cryptor.decrypt(byte)
        # 去除填充数据
        cipherbyte = self.un_padding(cipherbyte)
        return cipherbyte

# if __name__ == '__main__':
#     data = 'd437814d9185a290af20514d9341b710'
#     # data = FilePlugin.read_byte_from_file()
#     password = '78f40f2c57eee727a4be179049cecf89'  # 16,24,32位长的密码
#     encrypt_data = AESPlugin.encrypt(data, password)
#     encrypt_data = base64.b64encode(encrypt_data)
#     print('encrypt_data:', encrypt_data)
#
#     encrypt_data = base64.b64decode(encrypt_data)
#     decrypt_data = AESPlugin.decrypt(encrypt_data, password)
#     print('decrypt_data:', decrypt_data)
