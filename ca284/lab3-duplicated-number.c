#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {

    int num = 0;
    
    for (int i = 0; i < argc - 1; i++) {
        for (int j = i + 1; j < argc -1; j++) {
            if (strcmp(argv[i], argv[j]) == 0) {
                num = atoi(argv[j]);
            }
        }
    }
    if (num != 0) {
        printf("%d\n", num);
    }
    else {
        printf("no duplicated number\n");
    }
}
