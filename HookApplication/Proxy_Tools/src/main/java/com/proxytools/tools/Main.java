package com.proxytools.tools;

import java.io.File;
import java.io.FileOutputStream;
import java.io.FilenameFilter;
import java.io.RandomAccessFile;

/**
 * @author syl
 * @time 2021/12/28 14:38
 */
public class Main {

    public static void main(String[] args) throws Exception {
        String apkFileName = null;
        String proxyAppAARName = null;
        String signerFileName = null;
        String packageName = null;
        String newApkFileName = null;
        String key = null;
        String iv = null;
        if (args != null && args.length > 0) {
            for (String arg : args) {
                System.out.println(arg);
            }
            apkFileName = args[0];
            proxyAppAARName = args[1];
            signerFileName = args[2];
            packageName = args[3];
            newApkFileName = args[4];
            key = args[5];
            iv = args[6];
        }
        /**
         * 1、制作只包含解密代码的dex 文件
         */
        //1.1 解压aar 获得classes.jar
        File aarFile = new File(proxyAppAARName);
        File aarTemp = new File("file_output/aar_output/temp");
        Zip.unZip(aarFile, aarTemp);
        File classesJar = new File(aarTemp, "classes.jar");
        //1.2 执行dx命令 将jar变成dex文件
        File classesDex = new File(aarTemp, "classes.dex");
        Process process = Runtime.getRuntime().exec("cmd /c dx --dex --output " + classesDex
                .getAbsolutePath() + " " +
                classesJar.getAbsolutePath());
        process.waitFor();
        //失败
        if (process.exitValue() != 0) {
            throw new RuntimeException("dex error");
        }

        /**
         * 2、加密apk中所有dex文件
         */
        File apkFile = new File(apkFileName);
        File apkTemp = new File("file_output/apk_output/temp");
        Zip.unZip(apkFile, apkTemp);
        File[] dexFiles = apkTemp.listFiles(new FilenameFilter() {
            @Override
            public boolean accept(File file, String s) {
                return s.endsWith(".dex");
            }
        });
        for (File dex : dexFiles) {
            byte[] bytes = getBytes(dex);
            byte[] encrypt = EncryptUtil.encryptByte(bytes, key, iv);
            FileOutputStream fos = new FileOutputStream(new File(apkTemp, packageName + dex.getName().replace("dex", "xed")));
            fos.write(encrypt);
            fos.flush();
            fos.close();
            dex.delete();
        }

        /**
         * 3、把classes.dex 放入 apk解压目录 在压缩成apk
         */
        classesDex.renameTo(new File(apkTemp, "classes.dex"));
        File unSignedApk = new File(newApkFileName);
        Zip.zip(apkTemp, unSignedApk);

        /**
         * 4、对齐与签名
         */
        File alignedApk = new File("output/apk_output/app-unsigned-aligned.apk");
        process = Runtime.getRuntime().exec("cmd /c zipalign -f 4 " + unSignedApk
                .getAbsolutePath() + " " +
                alignedApk.getAbsolutePath());
        process.waitFor();
        //失败
        process.waitFor();
        if (process.exitValue() != 0) {
            throw new RuntimeException("zipalign error");
        }

        //4.2 签名
//        apksigner sign  --ks jks文件地址 --ks-key-alias 别名 --ks-pass pass:jsk密码 --key-pass
// pass:别名密码 --out  out.apk in.apk
        File signedApk = new File("apk/app-unsigned-aligned-sign.apk");
        File jks = new File("app/signature/" + signerFileName + ".jks");
        process = Runtime.getRuntime().exec("cmd /c apksigner sign  --ks " + jks.getAbsolutePath
                () + " --ks-key-alias yeyan --ks-pass pass:yeyan123 --key-pass  pass:yeyan123 --out" +
                " " + signedApk.getAbsolutePath() + " " + alignedApk.getAbsolutePath());
        process.waitFor();
        //失败
        if (process.exitValue() != 0) {
            throw new RuntimeException("apksigner error");
        }

    }

    public static byte[] getBytes(File file) throws Exception {
        RandomAccessFile r = new RandomAccessFile(file, "r");
        byte[] buffer = new byte[(int) r.length()];
        r.readFully(buffer);
        r.close();
        return buffer;
    }
}
