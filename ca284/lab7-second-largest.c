#include <stdio.h>
#include <stdlib.h>

void selectSort(float *pArray, int length);
void getSecondLargest(float *pArray, int length);

int main(int argc, char *argv[]) {

    int length = argc - 1;
    float *pArray = (float*)malloc(length*(sizeof(float)));
    int i;

    if (!pArray) {

        printf("Memory allocation failed!\n");
        return 0;
    }

    for (i = 0; i < length; i++) {

        *(pArray + i) = atof(argv[i + 1]);
    }

    selectSort(pArray, length);

    getSecondLargest(pArray, length);

    free(pArray);

    return 0;

}

void selectSort(float *pArray, int length) {

    int i, j, temp;

    for (i = 0; i < length; i++) {
        
        for (j = i + 1; j < length; j++) {

            if (*(pArray + j) < *(pArray + i)) {
                temp = *(pArray + i);
                *(pArray + i) = *(pArray + j);
                *(pArray + j) = temp;
            }

        }
    }

}

void getSecondLargest(float *pArray, int length) {

    int i = length - 1;

    while (*(pArray + i) == *(pArray + i - 1)) {

        i--;
    }

    if (*(pArray + i) != *pArray + i - 1) {
        printf("%.1f\n", *(pArray + i - 1));
    }

    else {
        printf("%.1f\n", *(pArray + length - 2));
    }
}