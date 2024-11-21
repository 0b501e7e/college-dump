import java.util.Scanner;

public class Reverse
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("How many numbers: ");
        int num = in.nextInt();
        int num2 = 0;
        int count = 0;
        int[] arr = new int[num];
        int[] arr2 = new int[num];

        System.out.print("Enter " + num + " numbers: ");
        // Read in the numbers
        for (num2 = in.nextInt(); count < num; num2 = in.nextInt() ) {
            arr[count] = num2;
            count += 1;
        }
        count = 0;

        for (int i = num; i != 0; i--) {
            arr2[count] = arr[i];
        }
        
        // reverse the numbers
        
        // print them out
        for (int i = 0; i < arr2.length; i++) {
            System.out.print(" " + arr2[i]);
        }
        System.out.println();
        // Use System.out.print(" " + num[i]); and finish with a newline.
    }
}