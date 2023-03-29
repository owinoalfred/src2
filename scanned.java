import java.util.Scanner;

public class scanned{
    public static void main(String[] args){

       Scanner name = new Scanner(System.in);
       String firsname = name.next();
       System.out.println("your firt name is : " + firsname);

       Scanner lastname = new Scanner(System.in);
       String nameLast = lastname.nextLine();
       System.out.println("your name is : " + nameLast);
        }
}