import java.util.*;
import java.util.Scanner;
class Main{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        String str=sc.nextLine();
        char arr[]=new char[str.length()];`
        //StringBuilder sb=new StringBuilder();
        for(int i=0;i<str.length();i++){
            arr[i]=str.charAt(i);
        }
        Arrays.sort(arr);
        str=new String(arr);
        System.out.println(str);

    }
}