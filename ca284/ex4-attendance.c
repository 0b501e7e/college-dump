/*
Author: Senan Warnock
Date: 9th of December
Description: This program takes n records for n students and prints out
a 1 or a 0 depending on how many absences they have.

We start by creating a pointer to an array for our input and filling it.
Then we write some functions to deal with finding the needed marks.
We write a function to find the number of A's in each array element and return it.
We write a function to find the number of 'LLL's in each array element and return it.
We then write a function to add these counts together, and if it is equal to or over
3, we print 1, otherwise we print 0.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//function prototypes
void printAttendance(char *arr[], int len);
int getA(char *arr, int len);
int getL(char *arr, int len);


int main(int argc, char *argv[]) {
    
    int i;
    char *(arr)[argc - 1];

    //loop to fill input into our array
    for (i = 0; i < argc - 1; i++) {
        
        arr[i] = argv[i + 1];
    }
    //print attendance results
    printAttendance(arr, argc - 1);

    return 0;

}

//function to get all 'LLL' in each element
int getL(char *arr, int len) {
    int i, j;
    int count = 0;
    char *el = "LLL";
    char *tmp = arr;

    while ((tmp = strstr(tmp, el))) {
        count++;
        tmp++;
    }
    return count;
    
}

//function to find all 'A's in each element
int getA(char *arr, int len) {
    int i;
    int count = 0;

    for (i = 0; i < len; i++) {
        
        if (*(arr + i) == 'A') {
                count += 1;
            }
    }
    return count;
}

//function to print results of attendance records
void printAttendance(char *arr[], int len) {

    int i, j;

    

    for (i = 0; i < len; i++) {

        //get counts
        int acount = getA(*(arr + i), strlen(*(arr + i)));
        int lcount = getL(*(arr + i), strlen(*(arr + i)));
        int actual = acount + lcount;

        //if we have 3 or more absences, print 1
        if (actual >= 3) {
            printf("%d\n", 1);
        }
        //or print 0
        else {
            printf("%d\n", 0);
        }
    }
}