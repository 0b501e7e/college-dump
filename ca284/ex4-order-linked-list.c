/*
Author: Senan Warnock
Date: 10th November
Description: This program creates a linked list from command
line arguments and checks whether its sorted in descending 
order.

We begin by defining the node type and declaring the node struct.
Then we write some functions to create and fill
the linked list with the command line data.
After, we use another function to loop through and make sure the
list is sorted in descending order, printing 1 or 0 depending on 
the answer.
*/
#include <stdio.h>
#include <stdlib.h>

//type creation
typedef struct Node Node;

// node structure declaration
struct Node {
    float data;
    Node *prev;
    Node *next;
};

void isDesc(Node *first);
Node* fillNode(int length, char*argv[]);


int main(int argc, char *argv[]) {

    //get length
    int length = argc - 1;

    Node *first = NULL;

    //fill nodes
    first = fillNode(length, argv);

    //check if list is in descending order
    isDesc(first);
    return 0;
}

//function to fill create linked list and fill nodes
Node* fillNode(int length, char*argv[]) {
    Node *first = NULL;
    Node *current = NULL;
    Node *prev = NULL;

    first = (Node*)calloc(1, sizeof(Node));
    current = first;

    //fill nodes with data
    for(int i = 0; i < length; ++i) {
        current->data = atof(argv[i + 1]);

        //Check if the last node
        if(i == length - 1) {
            current->next = NULL;
        } 
        else if (i == 0) { //check if first node
            current->prev = NULL;
            current->next = (Node*)calloc(1, sizeof(Node));
            prev = current;
            current = current->next;
            current->prev = prev;

        } 
        else {
            current->next = (Node*)calloc(1, sizeof(Node));
            prev = current;
            current = current->next;
            current->prev = prev;
        }
    }

    return current;
}

//function to check if is in descending order
void isDesc(Node *last) {
    
    Node *p = NULL;
    int flag;
    
    //traverse list and check if is descending
    for (p = last; p->prev != NULL; p = p->prev ) {
        if (p->data <= p->prev->data) {
            flag = 1;
        }
        
        //break if not descending
        else {
            flag = 0;
            break;
        }
    }

    //print result
    printf("%d\n", flag);
}