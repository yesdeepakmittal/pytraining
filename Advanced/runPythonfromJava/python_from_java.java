import java.io.*;

public class python_from_java {
    public static void main(String[] args) throws IOException {

        //reference - https://stackoverflow.com/a/27268010/16470401
        Process p = Runtime.getRuntime().exec("python C:\\Users\\deepak-mittal\\Desktop\\python_script.py");
//        BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
//        String result = in.readLine();
//        System.out.println("Result is : "+result);
    }
}
