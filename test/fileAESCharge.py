import os
import xml.etree.ElementTree as ET
from Crypto.Cipher import AES
import random
import string
import base64
import re

AES_SECRET_KEY = ''
IV = '1234567890123456'

# padding算法
BS = 0
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1:])]


# 加密函数
def encrypt(key, text):
    # 先对字段进行base64加密
    text = base64.b64encode(text)
    print('text:', text)
    cryptor = AES.new(key.encode("utf8"), AES.MODE_CBC, IV.encode("utf8"))
    print('text.decode', text.decode())
    ciphertext = cryptor.encrypt(bytes(pad(text.decode()), encoding="utf8"))
    print('ciphertext:', ciphertext)
    # AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
    print('result:', base64.b64encode(ciphertext))
    return base64.b64encode(ciphertext)


# 解密函数
def decrypt(key, text):
    # 先对字段进行base64解密
    print('decrypt_text:', text)
    decode = base64.b64decode(text)
    print('decrypt_decode:', decode)
    cryptor = AES.new(key.encode("utf8"), AES.MODE_CBC, IV.encode("utf8"))
    plain_text = cryptor.decrypt(decode)
    # 去除填充
    t = unpad(plain_text)
    print(t)
    print('decrypt_result:', base64.b64decode(t))
    return base64.b64decode(t)

if __name__ == '__main__':
    # 随机生成16位字符串
    # AES_SECRET_KEY = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    AES_SECRET_KEY = 'nDsbUJgokwEV7TBK'
    print(AES_SECRET_KEY)
    BS = len(AES_SECRET_KEY)

    encryptBytes = b''
    print('*' * 40)
    print('开始加密')
    #AES加密
    # 对目标文件进行只读处理 得到二进制流
    with open("classes4.dex", mode='rb') as f:
        content = f.read()
        encryptBytes = encrypt(AES_SECRET_KEY, content)
        f.flush()
        f.close()

    # 生成新的加密文件
    newEncryptFileName = 'new_classes4.xed'
    with open(newEncryptFileName, 'wb') as f:
        f.write(encryptBytes)
        f.flush()
        f.close()

    print('已生成加密文件')
    print('*' * 40)

    # print('开始解密')
    # decryptBytes = b''
    # with open(newEncryptFileName, mode='rb') as f:
    #     content = f.read()
    #     print('content:', content)
    #     decryptBytes = decrypt(AES_SECRET_KEY, content)
    #
    # #生成解密文件
    # newDecryptFileName = 'decrypt_classes.dex'
    # with open(newDecryptFileName, 'wb') as f:
    #     f.write(decryptBytes)
    #     f.flush()
    #     f.close()
    # print('解密结束')