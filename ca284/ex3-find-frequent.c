/*
Author: Senan Warnock

Date: 25th November

Description:

This program takes integer input and finds the most frequently occurring integers.

We start by allocating memory for 5 integers and slowly adding enough memory for another integer until we reach the
end of the command line input. We store these integers in an array, then we sort them for later.

Once sorted, we loop through them to count each item and if the item has a count of over 3, we put them in a new array and print them.
*/

#include <stdio.h>
#include <stdlib.h>

//function prototype
void sort(int n, int *arr);

int main(int argc, char *argv[]) {

    //some declarations etc
    int capacity = 5;
    int *pArray = (int*)calloc(capacity, sizeof(int));
    int i, j, count;
    int k = 0;
    int newArr[argc - 1]; 

    // add numbers to array while not at capacity
    for (i = 0; i < capacity; i++) {

        *(pArray + i) = atoi(argv[i + 1]);

    }
    //allocate more memory and add numbers as needed
    while (capacity < argc - 1) {

        int *pTemp = NULL;
        capacity += 1;
        pTemp = realloc(pArray, capacity * sizeof(int));
        if (!pTemp) {
            printf("Memory reallocation failed.\n");
            free(pArray);
            pArray = NULL;
            return 0;
        }
        pArray = pTemp;
        *(pArray + capacity - 1) = atoi(argv[capacity]);
    }

    //sort the array
    sort(capacity, pArray);

    //find count of each number and put them in the new array, then print.
    for (i = 0; i < argc - 1; i++) {
        
        count = 1;

        for (j = i + 1; j < argc - 1; j++) {

            if (*(pArray + i) == *(pArray + j)) {

                count++;
            }

        }
        if (count > 3) {
            
            for (j = 0; j < count; j++) {
                newArr[k] = *(pArray + i);
                printf("%d\n", newArr[k]);
                k++;
                
            }
        }

        else {

            continue;
        }
    }
    free(pArray);
    pArray = NULL;
    return 0;
}


// sort function
void sort(int n, int *arr) {
    int i, j, k;
  
    for (i = 0; i < n; i++) {
  
        for (j = i + 1; j < n; j++) {
  
            if (*(arr + j) < *(arr + i)) {
  
                k = *(arr + i);
                *(arr + i) = *(arr + j);
                *(arr + j) = k;
            }
        }
    }
}