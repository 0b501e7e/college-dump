/*
Author: Senan Warnock
Date: 11th of November
Description: This program takes attendance grades as strings from command line and prints a 1 if they have 2 or less absences or 0
if the have more than 2 absences.
We approach this program by first taking the input and creating an array of strings,
then we use nested for loops to traverse through each letter in each string and take a count
of the amount of 'A' characters in the string.
We then create an array of these results and use a function to print either a 1 or 0 depending on the result.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//function prototype
void printResults(int size, int *countArr);

int main(int argc, char *argv[]) {
    //some declarations
    int i, j;
    int size = argc - 1;
    char *arr[size];
    int count;
    int countArr[50];

    //loop to take input and fill the array
    for (i = 0; i < size; i++) {
       arr[i] = argv[i + 1];
    }

    //nested loops to traverse through each string in the array + create absence count
    for (i = 0; i < size; i++) {
        count = 0;
        for (j = 0; j < strlen(arr[i]); j++) {
            if (arr[i][j] == 'A') {
                count++;
           }
        }
        countArr[i] = count;
    }

    //function call to print results
    printResults(size, countArr);
    return 0;
}

//function to print results
void printResults(int size, int *countArr) {
    int i;
    for (i = 0; i < size; i++) {
        if (countArr[i] > 2) {
            printf("0\n");
        }
        else {
            printf("1\n");
        }
    }
}