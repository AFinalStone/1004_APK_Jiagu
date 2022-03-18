package test;

import java.io.FileWriter;
import java.io.IOException;

public class Test {

    public static void main(String[] arguments) {
        FileWriter fileWriter = null;
        try {
            fileWriter = new FileWriter("AndroidManifest_new.xml");
            fileWriter.write("你好啊");
            fileWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
