/*
Author: Senan Warnock

Description: This is a program to determine whether the entered
number is a triangular number in the given array. If it is,
it prints that it is a triangular number, and the contrary otherwise.

Date: 14th of October

We use a for loop to search through the array and use the found
variable to store an integer 1 if we have found it, then we print a
statement depending on the value of found
*/


#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {

    //variables to declare
    int tri[] = {1, 2, 6, 10, 15, 21, 28, 36, 45, 55};
    int i;
    int num = atoi(argv[1]);
    int found;


    // for loop to determine whether the input is in the array
    for (i = 0; i < 10; i++) {
        if (tri[i] == num) {
            found = 1;
        }
    }

    //if found is 1 we have our number
    if (found == 1) {
        printf("%d is a triangular number\n", num);
    }

    // case for if we didn't find our number
    else {
        printf("%d is not a triangular number\n", num);
    }

    return 0;
}