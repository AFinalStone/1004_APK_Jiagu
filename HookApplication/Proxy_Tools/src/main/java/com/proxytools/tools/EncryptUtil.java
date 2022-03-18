package com.proxytools.tools;

import java.io.File;
import java.io.RandomAccessFile;

import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

/**
 * @author syl
 * @time 2021/12/28 11:45
 */
public class EncryptUtil {

    private static final String ALGORITHM = "AES/CBC/PKCS5Padding"; // 加密算法

    /**
     * 加密
     *
     * @param data
     * @return
     */
    public static byte[] encryptByte(byte[] data, String key, String iv) {
        try {
            Cipher encryptCipher = Cipher.getInstance(ALGORITHM);
            SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes(), "AES");
            encryptCipher.init(Cipher.ENCRYPT_MODE, secretKeySpec, new IvParameterSpec(iv.getBytes()));
            return encryptCipher.doFinal(data);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    /**
     * 解密
     *
     * @param data
     * @return
     */
    public static byte[] decryptByte(byte[] data, String key, String iv) {
        try {
            Cipher decryptCipher = Cipher.getInstance(ALGORITHM);
            SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes(), "AES");
            decryptCipher.init(Cipher.DECRYPT_MODE, secretKeySpec, new IvParameterSpec(iv.getBytes()));
            return decryptCipher.doFinal(data);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public static byte[] getBytes(File file) throws Exception {
        RandomAccessFile r = new RandomAccessFile(file, "r");
        byte[] buffer = new byte[(int) r.length()];
        r.readFully(buffer);
        r.close();
        return buffer;
    }

}
