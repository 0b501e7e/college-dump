import java.util.Scanner;

public class Initial {

    public static void main(String [] args) {

        Scanner in = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = in.next();
        System.out.println(name + " starts with the letter " + name.substring(0, 1) + ".");
        in.close();
    }
}