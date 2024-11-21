
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
    int firstEven;
    int oddCount;

    for (i = 0; i < argc - 1; i++) {
        arr[i] = atoi(argv[i + 1]);
    }

    for (i = 0; i < argc - 1; i++) {
        if (arr[i] % 2 == 0) {
            firstEven = arr[i];
            break;
        }

        
    }
    
    for (i = 0; i < argc - 1; i++) {
        if (arr[i] % 2 == 1) {
            oddCount += arr[i];
        }
    }

    for (i = 0; i < argc - 1; i++) {
        if (arr[i] % 2 == 0 && arr[i] != firstEven) {
            firstEven -= arr[i];
        }
    }

    printf("%d\n", oddCount);
    printf("%d\n", firstEven);
}