public class Test
{
    // Create a static method called getSum which sums an array of ints

    public static int countEven(int[] arr) {
        int result = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % 2 == 0) {
                result += 1;
            }
        }
        return result;
    }
}