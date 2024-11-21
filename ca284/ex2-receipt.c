/*
Author: Senan Warnock
Date: 11th of November
Description: This program takes a shopping list input and creates a struct, prints
out the total price of all items.

We start by defining the type Shopping for save typing,
then we create a struct to store the different types of data and create an array of structs.
We then create a function to populate our struct array with all the different items.
Once we have done that, we write another function to handle the printing of the data.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//type definition for struct
typedef struct Shopping Shopping;

//function prototypes
void createStruct(int size, Shopping *cart, char *argv[]);
void printPrice(Shopping *cart, int size, float *pSum);
//struct declaration
struct Shopping {
    char name[20];
    int amount;
    float price;
    int promotion;
    char sale[20];
};

int main(int argc, char *argv[]) {
    
    //some declarations / initialisations
    Shopping cart[50];
    int size = argc - 1;
    float sum = 0;
    float *pSum = &sum;

    //function call to populate the struct
    createStruct(size, cart, argv);

    //function call to print data
    printPrice(cart, size, pSum);

    return 0;
}

//function to populate the struct
void createStruct(int size, Shopping *cart, char *argv[]) {

    int i = 1;
    int count = 0;

    //while condition holds, add data to each struct array member
    while (i < size) {
        strcpy(cart[count].name, argv[i]);
        i++;
        cart[count].amount = atoi(argv[i]);
        i++;
        cart[count].price = atof(argv[i]);
        i++;
        cart[count].promotion = atoi(argv[i]);
        if (cart[count].promotion == 1) {
            strcpy(cart[count].sale, "On Sale");
        }
        else {
            strcpy(cart[count].sale, "No Sale");
        }
        i++;
        count++;

    }
}

//function to print data
void printPrice(Shopping *cart, int size, float *pSum) {

    int i, j;
    int count = 0;;
    float saleSum = 0;

     for (i = 0; i < size / 4; i++) {
        if (cart[i].promotion == 1) {
            for (j = 1; j < cart[i].amount; j++) {
                if (j % 3 == 0) {
                    count++;
                }
            }
            saleSum = (cart[i].amount - count) * cart[i].price;
            count = 0;
            *pSum += saleSum;

        }
        else {
           *pSum += cart[i].price * cart[i].amount;
        }
        
        
    }
    printf("%.2f\n", *pSum);
}