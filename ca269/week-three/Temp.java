import java.util.Scanner;

public class Temp {

    public static void main(String [] args) {

        Scanner in = new Scanner(System.in);
        System.out.print("Give me a fahrenheit temperature: ");
        double tmp = in.nextDouble();
        double temp = Convert.fahr2cels(tmp);
        System.out.println("In Celsius that would be: " + temp);
    }
}