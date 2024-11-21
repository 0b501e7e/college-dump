/*
Author: Senan Warnock
Date: 11th of November
Description: This program takes integer inputs and turns it into a 2d matrix and prints the sum of the anti diagonal.

We start with assigning the integers to a 2d array.
Then we use a function to print the mth element, starting at the last element of the array,
and decrement on each loop iteration to give us the backwards diagonal pattern, which we sum up and return.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//function prototype
int sumAntiDiag(int (*pArr)[100], int n);

int main(int argc, char* argv[]) {
	
    //some declarations and assignments
    int n = atoi(argv[1]);
    int k = 2;
	int a[100][100];
	int (*pArr)[100] = a;

    //assign input to 2d array
	for (int i=0; i<n; i++) {
		for (int j=0; j<n; j++) {
			a[i][j] = atoi(argv[k]);
            k++;
    }
    }

    //print the sum using the function
	printf("%d\n", sumAntiDiag(pArr, n));
	return 0;
}

//function to sum up the diagonals
int sumAntiDiag(int (*pArr)[100], int n){
    int sum = 0;
    int i;
    int m = n - 1;

    for (i=0; i<n; i++) {
        sum += pArr[i][m];
        m--;
    }
    return sum;
}
