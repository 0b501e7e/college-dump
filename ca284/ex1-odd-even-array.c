/* Author: Senan Warnock

Description: This program takes integer inputs and separates odd
integers to sum them up and subtracts even integers from the first even integer.

Date: 14th of October 2021

We begin by declaring variables that will be needed, then
using a for loop, we will extract the numbers from stdin to form 
an array, from that array we will create a even integer
array and sum up the odd values otherwise. we also save the first
even number to subtract the rest of the even numbers.
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int i;
    int arr[argc - 1];
    int even[argc - 1];
    int j = 0;
    int countOdd;
    
    //for loop to extract command line arguments
    for (i = 0; i < argc - 1; i++) {
        arr[i] = atoi(argv[i + 1]);
    }

    //for loop to create an even number array or add odd numbers
    for (i = 0; i < argc - 1; i++) {
        if (arr[i] % 2 == 0) {
            even[j] = arr[i];
            j++;
        }
        else if (arr[i] % 2 == 1) {
            countOdd += arr[i];
        }

        else if (arr[i] = 0) {
            printf("0");
            return 0;
        }
        
    }
    //save the first even number
    int firstEven = even[0];

    //subtraction of the rest of the even integers from the first one using a for loop
    for (i = 1; i < argc / 2; i++) {
        firstEven -= even[i];
    }
    //print the results
    printf("%d\n", countOdd);
    printf("%d\n", firstEven);
    
    return 0;
}