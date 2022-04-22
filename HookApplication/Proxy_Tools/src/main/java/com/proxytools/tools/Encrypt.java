package com.proxytools.tools;

import java.io.File;
import java.io.FileOutputStream;

/**
 * @author syl
 * @time 2021/12/28 14:38
 */
public class Encrypt {

    public static void main(String[] args) throws Exception {
        String fileName = null;
        String resultFileName = null;
        String key = null;
        String iv = null;
        String type = null;
        if (args != null && args.length > 0) {
            for (String arg : args) {
                System.out.println(arg);
            }
            fileName = args[0];
            resultFileName = args[1];
            key = args[2];
            iv = args[3];
            type = args[4];
        }
        File file = new File(fileName);
        File resultFile = new File(resultFileName);
        byte[] bytes = EncryptUtil.getBytes(file);
        byte[] result = null;
        if ("encrypt".equals(type)) {
            result = EncryptUtil.encryptByte(bytes, key, iv);
        } else {
            result = EncryptUtil.decryptByte(bytes, key, iv);
        }
        FileOutputStream fos = new FileOutputStream(resultFile);
        fos.write(result);
        fos.flush();
        fos.close();
    }

}
