#!/usr/bin/python3
# -*- coding: utf-8 -*-
import base64
import binascii
import logging

from Crypto.Cipher import AES

from python.plugin.FilePlugin import FilePlugin


class AESCrypt:
    """
    AES/CBC/PKCS5Padding 加密
    """

    def __init__(self, key):
        """
        使用密钥,加密模式进行初始化
        :param key:
        """
        if len(key) != 16:
            raise RuntimeError('密钥长度非16位!!!')

        self.key = str.encode(key)
        self.iv = bytes(16)
        self.MODE = AES.MODE_CBC
        self.block_size = 16

        # # 填充函数
        # # self.padding = lambda data: data + (self.block_size - len(data) % self.block_size) * chr(self.block_size - len(data) % self.block_size)
        # # 此处为一坑,需要现将data转换为byte再来做填充，否则中文特殊字符等会报错
        # self.padding = lambda data: data + (self.block_size - len(data.encode('utf-8')) % self.block_size) * chr(
        #     self.block_size - len(data.encode('utf-8')) % self.block_size)
        # # 截断函数
        # self.unpadding = lambda data: data[:-ord(data[-1])]

    def aes_encrypt(self, plaintext):
        """
        加密
        :param plaintext: 明文
        :return:
        """
        try:
            # 填充16位
            padding_text = self.padding(plaintext).encode("utf-8")
            # 初始化加密器
            cryptor = AES.new(self.key, self.MODE, self.iv)
            # 进行AES加密
            encrypt_aes = cryptor.encrypt(padding_text)
            # 进行BASE64转码
            encrypt_text = (base64.b64encode(encrypt_aes)).decode()
            return encrypt_text
        except Exception as e:
            logging.exception(e)

    def aes_decrypt(self, ciphertext):
        """
        解密
        :param ciphertext: 密文
        :return:
        """
        try:
            # 密文必须是16byte的整数倍
            # if len(ciphertext) % 16 != 0:
            #     raise binascii.Error('密文错误!')
            cryptor = AES.new(self.key, self.MODE, self.iv)
            # 进行BASE64转码
            plain_base64 = base64.b64decode(ciphertext)
            # 进行ASE解密
            decrypt_text = cryptor.decrypt(plain_base64)
            # 截取
            plain_text = self.unpadding(decrypt_text.decode("utf-8"))
            return plain_text
        except UnicodeDecodeError as e:
            logging.error('解密失败,请检查密钥是否正确!')
            logging.exception(e)
        except binascii.Error as e:
            logging.exception(e)
        except Exception as e:
            logging.exception(e)

    # 待加密文本补齐到 block size 的整数倍
    def PadTest(self, bytes):
        while len(bytes) % AES.block_size != 0:  # 循环直到补齐 AES_BLOCK_SIZE 的倍数
            bytes += ' '.encode()  # 通过补空格（不影响源文件的可读）来补齐
        return bytes  # 返回补齐后的字节列表


if __name__ == '__main__':
    # 测试
    cryptor = AESCrypt('ZGJfXxZNGPqWAC53')
    bytes = FilePlugin.read_byte_from_file("classes.dex")
    aes_encrypt_str = cryptor.aes_encrypt(cryptor.PadTest(bytes))
    print(f'加密结果为: {aes_encrypt_str}')
    aes_decrypt_str = cryptor.aes_decrypt('KMpLeX7zYGc3SBZi55/BR0VnMybZb29CrFJFl3ac8/k=')
    print(f'解密结果为: {aes_decrypt_str}')
