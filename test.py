import base64

from Crypto.Cipher import AES

from python.plugin.FilePlugin import FilePlugin


class Encrypt:
    def __init__(self, key, iv):
        self.key = key.encode('utf-8')
        self.iv = iv.encode('utf-8')

    def pkbyte7padding(self, byte):
        """
        明文使用PKCS7填充
        """
        bs = 16
        padding_size = len(byte)
        temp = padding_size % bs
        padding = bs - temp
        padding_text = padding * padding
        self.coding = padding
        return byte + padding_text


    def aes_encrypt(self, content_padding):
        """
        AES加密
        """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        # 处理明文
        content_padding = self.pkbyte7padding(content)
        # 加密
        encrypt_bytes = cipher.encrypt(content_padding.encode('utf-8'))
        # 重新编码
        result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
        return result

    def aes_decrypt(self, content):
        """
        AES解密
        """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        content = base64.b64decode(content)
        text = cipher.decrypt(content).decode('utf-8')
        return text.rstrip(self.coding)


if __name__ == '__main__':
    iv = '01pv928nv2i5ss68'
    key = '63f09k56nv2b10cf'
    a = Encrypt(key=key, iv=iv)
    bytes = FilePlugin.read_byte_from_file("奇乐直播.apk")
    content_padding = a.pkbyte7padding(bytes)
    e = a.aes_encrypt(content_padding)
    d = a.aes_decrypt(e)
    print("加密:", e)
    print("解密:", d)
