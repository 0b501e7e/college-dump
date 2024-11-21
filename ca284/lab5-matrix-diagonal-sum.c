/*
Author: Senan Warnock

Description: This program is used to calculate the sum of a matrix diagonal, with the first integer argument 
determining how the square size of the matrix.

Date: 28th of October

We begin by taking the numbers used to create the array.
Then we initialize another array and another variable.
Using the formula of the number for the square size + 1 we can get
each number used to sum for the diagonal. We then use a loop in the function
to sum up the resulting integers and print our answer.
*/

#include <stdio.h>
#include <stdlib.h>

//function prototype
void matrixSum(int prod, int *arr[], int *ans);

int main(int argc, char *argv[]) {

    //first argument for square size
    int prod = atoi(argv[1]);

    //array for the integers
    int string[argc - 1];
    
    int i = 2;
    int j = 0;

    //for loop to add integers to the array
    for ( i = 2; i < argc; i++) {
        string[j] = atoi(argv[i]);
        j++;

    }
    //pointers 
    int *ans = &string[0];
    int *arr[10];
    arr[0] = &string[0];

    matrixSum(prod, arr, ans);
    
    return 0;
}
//function to calculate matrix diagonal sum.
void matrixSum(int prod, int *arr[], int *ans) {
    
    int i = 1;

    //loop to create an array of diagonal numbers.
    while (i <= prod) {
        arr[i] = ans += prod + 1;
        i++;
    }

    int answer = 0;

    //loop to get the sum.
    for (i = 0; i < prod; i++) {
        
        answer += *arr[i];
    }
    printf("%d\n", answer);
}