from Crypto.Cipher import AES

AES_SECRET_KEY = '1234567890123456'
IV = '1234567890123456'


# 待加密文本补齐到 block size 的整数倍
def padding(bytes):
    while len(bytes) % AES.block_size != 0:  # 循环直到补齐 AES_BLOCK_SIZE 的倍数
        bytes += ' '.encode()  # 通过补空格（不影响源文件的可读）来补齐
    return bytes  # 返回补齐后的字节列表


# 待加密文本补齐到 block size 的整数倍
def un_padding(bytes):
    while len(bytes) % AES.block_size != 0:  # 循环直到补齐 AES_BLOCK_SIZE 的倍数
        bytes -= ' '.encode()  # 通过补空格（不影响源文件的可读）来补齐
    return bytes  # 返回补齐后的字节列表


# 加密函数
def encrypt_byte(byte):
    # 填充数据
    byte = padding(byte)
    cryptor = AES.new(str.encode(AES_SECRET_KEY), AES.MODE_CBC, str.encode(IV))
    ciphertext = cryptor.encrypt(byte)
    return ciphertext


# 解密函数
def decrypt_byte(byte):
    cryptor = AES.new(str.encode(AES_SECRET_KEY), AES.MODE_CBC, str.encode(IV))
    cipherbyte = cryptor.decrypt(byte)
    # 去除填充数据
    cipherbyte = un_padding(cipherbyte)
    return cipherbyte


if __name__ == '__main__':
    # AES加密
    # 对目标文件进行只读处理 得到二进制流
    with open("classes.dex", mode='rb') as f:
        content = f.read()
        encryptBytes = encrypt_byte(content)
        f.flush()
        f.close()

    # 生成新的加密文件
    newEncryptFileName = 'new_classes.xed'
    with open(newEncryptFileName, 'wb') as f:
        f.write(encryptBytes)
        f.flush()
        f.close()

    print('开始解密')
    decryptBytes = b''
    with open(newEncryptFileName, mode='rb') as f:
        content = f.read()
        print('content:', content)
        decryptBytes = decrypt_byte(content)

    # 生成解密文件
    newDecryptFileName = 'decrypt_classes.dex'
    with open(newDecryptFileName, 'wb') as f:
        f.write(decryptBytes)
        f.flush()
        f.close()
    print('解密结束')
