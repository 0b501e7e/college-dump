/*
Author: Senan Warnock;

Description: 
This program checks if a string from input is symmetrical or not.
We do this by splitting the string in half and reversing the second half
and if they are equal than we know they are symmetrical.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//function prototype
char reverse(char *str, int len);


int main(int argc, char *argv[]) {

    //variables and arrays to declare
    int i;
    int leng = sizeof(atoi(argv[1]) / sizeof(atoi(argv[0])));
    char *word;
    word = argv[1];
    char half1[leng / 2];
    char half2[leng / 2];
    
    //for loop to grab the first half of the string array
    for (i = 0; i < leng / 2 + 2; i++) {
        half1[i] = word[i];
    }
    
    // for loop to grab the 2nd half of the string array
    int j = 0;
    for (i = leng / 2 + 3; i <= strlen(word); i++) {
        half2[j] = word[i];
        j++;
    }

    //function to reverse the second half
    reverse(half2, strlen(half2));

    //if equal halfs, print yes, otherwise print no
    if (strcmp(half1, half2) == 0) {
        printf("yes\n");
    }
    else {
        printf("no\n");
    }
    return 0;
}

// function to reverse a string array in places
char reverse(char *str, int len) {
    char *pstr = str;
    char *pstr2 = str + len - 1;

    while (pstr < pstr2) {
        char tmp = *pstr;
        *pstr++ = *pstr2;
        *pstr2-- = tmp;
    }
    return *str;
}