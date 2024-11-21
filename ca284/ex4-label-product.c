/*
Author: Senan Warnock
Date: 10th of December
Description: This program takes command line input,
creates a data structure of items in a cart, updates its
items status depending on if the sales are above average.
Then finally it prints the name of the country of origin
and the status of each item.

We begin by defining the node struct type and declaring the
node structure. We then use a function to create a linked list to fill 
the nodes with all the command line arguments.
We then use two functions, once to get the average sales and another
to update the status of each node depending on the sales of each item.
Finally, we print the status and country of origin of each item.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//node type definition
typedef struct Node Node;

//function prototypes
void printNode(Node *first);
Node* fillNode(int length, char *argv[]);
Node* updateStatus(Node *first);

//node struct
struct Node {
    char itemCode[20];
    float price;
    int number;
    int status;
    Node *next;
};

int main(int argc, char *argv[]) {

    int length = (argc - 1)/3;

    //initialise first node
    Node *first = NULL;

    //fill nodes with command line info
    first = fillNode(length, argv);

    //update status of each node
    updateStatus(first);

    //print status and origin
    printNode(first);

    //free memory
    free(first);

    return 0;
}

//function to fill up the nodes from command line
Node* fillNode(int length, char *argv[])
{
    Node *first = NULL;
    Node *current = NULL;

    first = (Node*)calloc(1, sizeof(Node));
    current = first;

    int index = 1;

    //loop to get data
    for(int i = 0; i < length; ++i)
    {
        strcpy(current->itemCode, argv[index]);
        current->price = atof(argv[index + 1]);
        current->number = atoi(argv[index + 2]);
        current->status = 0;


        //Check if the last node
        if (i == length - 1){
            current->next = NULL;
        } 
        else {
            current->next = (Node*)calloc(1, sizeof(Node));
            current = current->next;
            index += 3;
        }
    }

    return first;
}

//function to print the node status and origin
void printNode(Node *first) {
    Node* p = NULL;
    int i = 0;
    char *codes[] = { "IE", "FR", "SP", "US", "RU" };
    char *origin[] = { "Ireland", "France", "Spain", "USA", "Russia"};
    
    //loop to print status, origin and match code to origin
    for(p = first; p != NULL; p = p->next) {
        for (i = 0; i < sizeof(codes) / sizeof(codes[0]); i++) {
            if (strstr(p->itemCode, codes[i]) != NULL) {
                printf("%d\n", p->status);
                printf("%s\n", origin[i]);
            }
        }
         
    }
}

//function to get sales average of all nodes
int getAverage(Node *first) {
    Node *p = NULL;
    p = first;
    int average;
    int sum = 0;
    int sales = 0;
    int salesCount = 0;
    for (p = first; p != NULL; p = p->next) {

        sales += p->price * p->number;
        salesCount++;
    }
    average = sales / salesCount;
    return average;
}

//function to update the status of each node
Node* updateStatus(Node *first) {
    Node *p = NULL;
    p = first;
    int average = getAverage(first);
    for (p = first; p != NULL; p = p->next) {
        
        int sales = p->price * p->number;
        if (sales >= average) {
            p->status = 1;
        }
        else {
            p->status = 0;
        }
    }
    return p;
}