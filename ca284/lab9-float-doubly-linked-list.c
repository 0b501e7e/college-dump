/*
Author: Senan Warnock
Date: 22nd of November
Description: This program takes integer input and creates a doubly linked list and prints it out in reverse.

We start by defining the node structure.
we then create a node by allocating memory to a pointer and using two pointers to keep track
of the previous and current node.
We then use a while loop to take the data and fill the node, checking to make sure we
don't create too many nodes.
Finally we print out the list in reverse order with the help of a function.
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

//function prototype
void printReverse(Node *last);

int main( int argc, char *argv[]) {

    int length = atoi(argv[1]);
    int i;
    //pointers to capture positions
    Node *head, *current, *prev;

    //create first node and point current to this node
    head = malloc(sizeof(Node));
    current = head;
    i = 0;

    //take data into the list and check to make sure we don't create too many
    while (i < atoi(argv[1])) {

        current -> data = atof(argv[i + 2]);
        if (i < length - 1) {
            current -> next = malloc(sizeof(Node));
            prev = current;
            current = current -> next;
            current -> prev = prev;
            
        }
        i++;
    }
    current -> next = NULL;
    
    printReverse(current);
    free(head);
    return 0;
}
//function to print in reverse
void printReverse(Node *last) {

    Node *ptr = NULL;

    for (ptr = last; ptr != NULL; ptr = ptr -> prev) {
        printf("%.2f\n", ptr -> data);
    }
}