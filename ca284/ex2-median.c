/*
Author: Senan Warnock
Date: 11th of November
Description: This program calculates what the centre characters of a given list of integers are.

First, we take the integers from input and create an array. Then we write a function to sort the array and then we calculate the middle values.
Under the assumption that the integer array is even, we can calculate as follows:
if we have 10 integers from 1 - 10:
the middle value would 5, putting array[5] would give us 6 since we start counting from 0.
therefore it should be 10 / 2 - 1 to give us 5 in the array.
Since this array is even, one number does not split the array evenly, so then we also take the next integer, 10 / 2 which would give us 6.
This splits the array evenly on both sides, meaning we have our centre numbers.
*/


#include <stdio.h>
#include <stdlib.h>
//function prototype
void sortArray(int size, int *pArray);

int main(int argc, char *argv[]) {

    //some variable declarations.
    int size = argc - 1;
    int arr[size];
    int i;

    //for loop to take input and place in our array.
    for (i = 0; i < size; i++) {
        arr[i] = atoi(argv[i + 1]);
    }
    //function call to sort the array in ascending order.
    sortArray(size, arr);

    // resulting centre numbers array
    int result[] = {arr[size / 2 - 1], arr[size / 2]};

    //get the new size of this array for the coming for loop
    int newsize = sizeof(result) / sizeof(result[0]);

    //print the centre numbers in result.
    for (i = 0; i < newsize; i++) {
        printf("%d\n", result[i]);
    }
    
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