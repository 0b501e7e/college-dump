/*
Author: Senan Warnock
Date: 11th of November
Description: This program calculates the degree of an integer array given from input.
First we create an array from the given input. We then use nested for loops
to count each appearance of an integer along the array. Some numbers will be counted more than
once but for our purposes in doesn't matter as the max count of a number will still show up.
We take each count and put it in a new array, which we sort and print the last member of that array,
being the degree of the array.
*/

#include <stdio.h>
#include <stdlib.h>

//function prototype
void sortArray(int size, int *pArray);

int main(int argc, char *argv[]) {

    //declarations
    int i, j;
    int size = argc - 1;
    int count;
    int countArr[size];
    int arr[size];

    //create array from input
    for (i = 0; i < size; i++) {
        arr[i] = atoi(argv[i + 1]);
    }

    //nested loops to count each incidence of each integer in the array
    for (i = 0; i < size; i++) {
        count = 1;
        for (j = i + 1; j < size; j++) {
            if (arr[j] == arr[i]) {
                count++;
            }
        }
        countArr[i] = count;
    }

    //function call to sort our array of frequencies
    sortArray(size, countArr);

    //print out the last integer in the array, after sorting, this is the degree.
    printf("%d\n", countArr[size - 1]);

    return 0;
}

void sortArray(int size, int *pArray) {

    int i, j, k;

    for (i = 0; i < size; i++) {

        for (j = i + 1; j < size; j++) {

            if (*(pArray + j) < *(pArray + i)) {

                k = *(pArray + i);
                *(pArray + i) = *(pArray + j);
                *(pArray + j) = k;
            }
        }
    }
}