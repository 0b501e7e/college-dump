import java.util.Scanner;

public class NoMinusOne {

    public static void main(String [] args) {

        Scanner in = new Scanner(System.in);

        System.out.println("Enter numbers: ");

        int num = 0;
        int prev = 0;

        for (num = in.nextInt(); num > 0; num = in.nextInt()) {
            prev = num;

        }
        
        System.out.println("The penultimate number was: " + prev);
    }
}