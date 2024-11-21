//
// Supplied code to help ensure there will be no output formatting issues.
//
import java.util.Scanner;

public class AboveAverage
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        System.out.print("How many numbers: ");
        int num = in.nextInt();
        
        float[] arr;
        float num2 = 0;
        int count = 0;
        float total = 0;
        
        System.out.print("Enter " + num + " numbers: ");
        arr = new float[num];
        // Now read in the numbers
        for (num2 = in.nextFloat(); count < num; num2 = in.nextFloat() ) {
            arr[count] = num2;
            total += num2;
            count += 1;
            if (count == num) {
                break;
            }
        }

        float average = total / num;
        
        // Print out the numbers greater than the average
        System.out.println("The above average numbers are:");
        // You can use the following code to print out one number
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > average) {
                System.out.print(" " + arr[i]); // You may want to put this in a loop.

            }
        }
       
        System.out.println(); // Should finish with a new line
    }
}