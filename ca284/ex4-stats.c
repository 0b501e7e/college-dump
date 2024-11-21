/*
Author: Senan Warnock
Date: 9th of December
Description: This program takes integer inputs and computes
either the max number, the mode or the standar deviation depending
on the last integer input.

We start by taking in the last integer which will be our choice for the function
to be used.
We then create an array from the command line arguments.
We then use some control flow statements to say what operation must happen.
We use function pointers to point the functions, and the choice argument will be used
to decide which function operation will happen.
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//function prototypes
void (*choose_function[]) (int *arr, int len);
void max(int arr[], int len);
void mode(int arr[], int len);
void stdev(int arr[], int len);



int main(int argc, char *argv[]) {

    //choice variable
    int choice = atoi(argv[argc - 1]);
    int arr[argc - 2];
    int i;

    //loop to populate array
    for (i = 0; i < argc - 2; i++) {
        arr[i] = atoi(argv[i + 1]);
    }

    //length of array
    int len = sizeof(arr) / sizeof(arr[0]);

    //if choice is greater than 3 or is 0, choose option 1
    if (choice > 3 || choice == 0) {
        (*choose_function[1]) (arr, len);
    }
    
    //otherwise, do choice
    else {
        (*choose_function[choice]) (arr, len);
    }
    return 0;

}

//function pointer to choose function to use
void (*choose_function[]) (int *arr, int len) = {max, max, mode, stdev};

//function to find max integer in the array
void max(int arr[], int len) {
    
    int i, max = 0;

    //loop to find max
    for (i = 0; i < len; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    printf("%d\n", max);
}

//function to find the mode of the array
void mode(int arr[], int len) {
    
    int i, j; 
    int count = 0;
    int maxCount = 0;
    int mode;

    //for loop to get frequency of each element
    for( i = 0; i < len; i++) {
        count = 0;
        for (j = 0; j < len; j++) {
            if (arr[i] == arr[j]) {
                count++;
            }
        }
        if (count > maxCount) {
            maxCount = count;
            mode = arr[i];
        }
    }
    printf("%d\n", mode);
}

//function to find the standard deviation of the array
void stdev(int arr[], int len) {

    float sum = 0.0, mean; 
    float stdev = 0.0;
    int i;

    //get sum of array elements
    for (i = 0; i < len; ++i) {
        sum += arr[i];
    }

    //get mean
    mean = sum / len;

    //get variance
    for (i = 0; i < len; ++i)
        stdev += pow(arr[i] - mean, 2);
    
    //print standard deviation
    printf("%.2f\n", sqrt(stdev / len));
}
