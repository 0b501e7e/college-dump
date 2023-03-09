/* 
Author: Senan Warnock

Description: This program takes inputs and a requirement print either the
largest or smallest number in the list of input floating point numbers

Date: 14th of October 2021

We use a basically use a for loop to extract the floating point numbers
and then apply the selection sort algorithm in a function to sort the numbers.
Once we have that, we use the condition about whether the requirement is largest
or smallest to print out the desired output.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//function prototype
void sortNums(float arr[], int num);

int main(int argc, char *argv[]) {

    //array and variables as well as n for array size
    float nums[argc - 1];
    int i;
    int res;
    int n = sizeof(nums) / sizeof(nums[0]);

    //for loop to extract the floating numbers
    for (i = 0; i <  argc - 1; i++) {
        nums[i] = atof(argv[i + 1]);
    }

    //use of function to sort numbers in array
    sortNums(nums, n);

    //logic to print output
    if (strcmp(argv[1], "largest") == 0) {
        printf("%.2f\n", nums[n - 1]);
    }
    else if (strcmp(argv[1], "smallest") == 0) {
        printf("%.2f\n", nums[1]);
    }

   

}

//function logic to sort numbers in array
void sortNums(float arr[], int n) {
    int i;
    int j;
    int min;

    for (i = 0; i < n - 1; i++) {
        min = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[min]) {
                min = j;
            }
        
        float tmp = arr[min];
        arr[min] = arr[i];
        arr[i] = tmp;
    }
}
}