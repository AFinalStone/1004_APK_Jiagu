package com.proxytools.tools;

import java.io.File;
import java.io.FileOutputStream;
import java.io.FilenameFilter;
import java.io.RandomAccessFile;

/**
 * @author syl
 * @time 2021/12/28 14:38
 */
public class JiaGu {

    public static void main(String[] args) throws Exception {
        String apkFileName = null;
        String proxyAppAARName = null;
        String packageName = null;
        String newApkFileName = null;
        if (args != null && args.length > 0) {
            for (String arg : args) {
                System.out.println(arg);
            }
            apkFileName = args[0];
            proxyAppAARName = args[1];
            packageName = args[2];
            newApkFileName = args[3];
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
            byte[] encrypt = EncryptUtils.getInstance().encrypt(bytes);
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
    }

    public static byte[] getBytes(File file) throws Exception {
        RandomAccessFile r = new RandomAccessFile(file, "r");
        byte[] buffer = new byte[(int) r.length()];
        r.readFully(buffer);
        r.close();
        return buffer;
    }
}
