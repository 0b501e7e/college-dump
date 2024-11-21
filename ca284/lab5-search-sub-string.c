#include <stdio.h>
#include <string.h>

void searchString(char *sentence, char *word);

int main(int argc, char *argv[]) {

    char *word = argv[2];
    char *sentence = argv[1];

    searchString(sentence, word);

    return 0;
}

void searchString(char *sentence, char *word) {

    char *pFound = strstr(sentence, word);

    if (pFound != NULL) {
        long index = pFound - &sentence[0];
        long end = index + strlen(word) - 1;
        printf("%ld %ld\n", index, end);
    }
    else {
        printf("Not found\n");
    }
}
    