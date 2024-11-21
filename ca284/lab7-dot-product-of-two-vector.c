#include <stdio.h>
#include <stdlib.h>

void calcDotProduct(int *pvectorArray, int length);

int main(int argc, char *argv[]) {

    int length = argc - 1;
    int vectorSize = atoi(argv[1]);
    int *pvectorArray = (int*)malloc(length*(sizeof(int)));
    int i;


    if (!pvectorArray) {
        printf("Failed to allocate memory!\n");
        return 1;
    }

    for (i = 0; i < length; i++) {
        *(pvectorArray + i) = atoi(argv[i + 2]);    
    }

    calcDotProduct(pvectorArray, vectorSize);

    
}

void calcDotProduct(int *pvectorArray, int length) {
    int result;
    int i;

    for (i = 0; i < length; i++) {

        result += pvectorArray[i] * pvectorArray[i + 3];
    }
    printf("%d\n", result);
}