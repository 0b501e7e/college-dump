/*
Author: Senan Warnock

Description: 
This program takes integer inputs specifying a range which we check whether the numbers in the range
are leap years and prints them if they are.

Date: 15th of October

we write a function to check whether the given year is a leap year
then we add it to an array inside the function,
then we use a for loop to print out the array containing the leap years.
*/

#include <stdio.h>
#include <stdlib.h>

// function prototype
void leapYears(int start, int stop, int n);

int main(int argc, char *argv[]) {

    

    // variables for start and end year
    int start;
    int stop;

    start = atoi(argv[1]);
    stop = atoi(argv[2]);


    //check if not less than minimum
    if (start < 1582) {
        return 0;
    }
        
    //check if not over maximum
    else if (stop > 2020) {
        return 0;
    }
    
    //function call to go through the numbers and print out the leap years
    leapYears(start, stop, argc + 1);
    
    return 0;
}
//function logic
void leapYears(int start, int stop, int n) {

    int arr[n];
    int i = 0;

    for (start = start; start <= stop; start++) {
        
        //if a number is divisible by 4 and 100 and 400... leap year, add to array
        if (start % 4 == 0 && start % 100 == 0 && start % 400 == 0) {

            arr[i] = start;
            i++;
        }
        // if a number is divisible by 4 and not by 100... leap year, add to array
        else if (start % 4 == 0 && start % 100 != 0) {
            
            arr[i] = start;
            i++;
        }
        
    }
    
    // for loop to print out the leap years in the array and stop after we reach the end year
    for (i = 0; i < n; i++) {
        if (arr[i] == stop) {
            printf("%d\n", arr[i]);
            break;
        }
        else {
            printf("%d\n", arr[i]);
        }
    }
}