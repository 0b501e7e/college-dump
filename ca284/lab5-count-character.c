/*
Author: Senan Warnock

Description: This program counts characters that appear in a string

Date: 23rd of October

we begin by assigning the arguments to pointers, then we build a function to loop through
the sentence and keep a count of the amount of times we match with our character.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//function prototype
void returnCount(char *letter, char *sentence);

int main(int argc, char *argv[]) {

    //pointers to arguments
    char *letter;
    letter = argv[1];
    char *sentence;
    sentence = argv[2];

    //function
    returnCount(letter, sentence);

}

//function logic
void returnCount(char *letter, char *sentence) {
    int count = 0;
    int i;

    //for loop to loop through the sentence and keep count
    for (i = 0; i < strlen(sentence); i++) {
        if (*letter == sentence[i]) {
            count++;
        }
    }

    printf("%d\n", count);
}