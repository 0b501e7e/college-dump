#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    int length = argc - 1;
    int arr[length];
    int i;
    int j = 0;

    for (i = 1; i <= length; i++) {
        arr[j] = atoi(argv[i]);
        j++;
    }

    for (int c = 0; c < length - 1; c++) {
        for (int d = 0; d < length - c - 1; d++) {
            if (arr[d] > arr[d + 1]) {
                int temp;
                temp = arr[d];
                arr[d] = arr[d + 1];
                arr[d + 1] = temp;
            }
        }
    }

    int k;
    for (k = 0; k < length; k++) {
        printf("%d\n", arr[k]);
    }
}