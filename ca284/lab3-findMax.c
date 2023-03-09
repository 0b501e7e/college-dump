#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void findMax(int arr[], int n);

int main(int argc, char *argv[]) {
    int length = argc - 1;
    int arr[length];
    int i;
    int j = 0;

    for (i = 1; i <= length; i++) {
        arr[j] = atoi(argv[i]);
        j++;
    }

    findMax(arr, length);
    return 0;
}

void findMax(int arr[], int n) {
    int i;

    int max = arr[0];

    for (i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    
    }
    printf("%d\n", max);
}