#include <stdio.h>

int main() {

    int arr[] = {0, 1, 2, 3, 4, 5};

    int *p = NULL;

    p = &arr[0];

    p -= 1;

    printf("%d\n", *p);
}