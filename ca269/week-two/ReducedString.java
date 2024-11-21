import java.util.Scanner;

public class ReducedString {

    public static void main(String [] args) {

        Scanner in = new Scanner(System.in);
        System.out.print("Enter an integer and a string: ");
        int pos = in.nextInt();
        String name = in.next();
        System.out.println(name.substring(0, pos) + name.substring(++pos));
        in.close();
    }
}