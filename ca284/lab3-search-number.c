#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    int find = atoi(argv[1]);
    int i;
    int arr[50];
    int length = argc - 1;
    int j = 0;
    int pos = 0;

    for (i = 2; i <= length; i++) {
        arr[j] = atoi(argv[i]);
        j++;
    }

    for (i = 0; i < length; i++) {
        if (arr[i] == find) {
            pos = i;
            printf("Found %d at %d\n", find, pos);
        }
    }

return 0;
}