package com.proxytools.tools;

import java.io.File;
import java.io.FileOutputStream;

/**
 * @author syl
 * @time 2021/12/28 14:38
 */
public class Decrypt {

    public static void main(String[] args) throws Exception {
        String fileName = null;
        String decryptFileName = null;
        String key = null;
        String iv = null;
        if (args != null && args.length > 0) {
            for (String arg : args) {
                System.out.println(arg);
            }
            fileName = args[0];
            decryptFileName = args[1];
            key = args[2];
            iv = args[3];
        }
        File file = new File(fileName);
        File decryptFile = new File(decryptFileName);
        byte[] bytes = EncryptUtil.getBytes(file);
        byte[] decrypt = EncryptUtil.decryptByte(bytes, key, iv);
        FileOutputStream fos = new FileOutputStream(decryptFile);
        fos.write(decrypt);
        fos.flush();
        fos.close();
    }


}
