/*
Author: Senan Warnock

Description: A program to check which character occurs most frequently

Date: 26th of October

For this program we write a function which creates an ascii array to handle any character that we might encounter.
For each char in the string, we count up that ascii value, giving us the count for each letter.
We then use a for loop to loop through and find the max count and at what position it is with index, giving us the position of the letter
which has the highest count.
*/

#include <stdio.h>
#include <stdlib.h>

//function prototype
void maxChar(char *sentence);

int main(int argc, char *argv[]) {
    //pointer to string
    char *sentence;
    sentence = argv[1];
    
    maxChar(sentence);

    return 0;
}


//function logic
void maxChar(char *sentence) {

    //create ascii array for letter codes
    int ascii_array[256] = {0};
    int i, max, index;

    //count through each ascii code we encounter
    for (i = 0; sentence[i] != 0; i++) {

        if (sentence[i] != 32) {
        ++ascii_array[sentence[i]];
        }
    }

    

    max = ascii_array[0];
    index = 0;

    // loop through to find the max character and the index
    for(i = 0; sentence[i] != 0; i++) {
        if( ascii_array[sentence[i]] > max) {
            max = ascii_array[sentence[i]];
            index = i;
     }
}
    //print the character at the index in the string
    printf("%c\n", sentence[index]);
}