import java.util.Scanner;

public class Cent2Fahr
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);
        
        // Find out how many inches (use a whole number for integers)
        int celsius = in.nextInt();
        double fahr = (celsius * 9.0/5.0) + 32;

        // Print out the result
        System.out.println(celsius + " " + fahr);
        in.close();
    }
}