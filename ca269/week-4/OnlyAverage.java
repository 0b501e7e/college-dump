import java.util.Scanner;

public class OnlyAverage
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        System.out.print("How many numbers: ");
        int num = in.nextInt();
        
        System.out.print("Enter " + num + " numbers: ");

        // Read in the numbers (note that they could be floating point)
        float num2 = 0;
        double total = 0;
        int count = 0;

        for (num2 = in.nextFloat(); count < num ; num2 = in.nextFloat() ) {
            total += num2;
            count += 1;
            if (count == num) {
                break;
            }
        }
        
        double average = total / num;
        // and calculate the average (or calculate the average as you read the numbers => no need for an array)
            
        System.out.println("The average is " + average);
    }
}