/*
Author: Senan Warnock

Description: 
This program takes an input integer and prints out a 
hailstone sequence based on the input integer.

Date: Senan Warnock

We write a function to deal with the logic of implementing
a hailstone sequence, then we first print the input number,
after that we use a while loop to continue the function
until we reach 1.
*/


#include <stdio.h>
#include <stdlib.h>

//function prototype
int hailstone(int num);

int main(int argc, char *argv[]) {
    int start = atoi(argv[1]);

//print input integer
printf("%s ", argv[1]);

    //while loop continuing the pattern until we reach 1
    while (start != 1) {
        start = hailstone(start);
        
        //if number is not 1 we add a space, otherwise no space
        if (start != 1) {
        printf("%d ", start);
        }
        else {
            printf("%d\n", start);
        }
    }
    return 0;
}
// function to create hailstone sequence
int hailstone(int num) {
    if (num % 2 == 0) {
        return num /= 2;
    }
    else {
        return num = 3 * num + 1;
    }
}