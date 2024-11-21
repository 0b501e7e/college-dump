/*

Author: Senan Warnock
Date: 21st of November
Description: This program takes integer input and converts it to a linked list, then prints the output.

We start by defining the linked list structure, then allocating memory for the first node.
We then use a for loop to assign each argument to each node in the linked list, checking to make
sure we are not creating too many nodes also.
Once we have the linked list we print it with a function, free the memory and exit.

*/
#include <stdio.h>
#include <stdlib.h>

//create Node type
typedef struct Node Node;

//Node definition
struct Node {
    int data;
    Node *link;
};
//function prototype
void printList(Node *head);

int main(int argc, char *argv[]) {

    int i;

    Node *head, *current;

    //create first node and point current to head
    head = malloc(sizeof(Node));
    current = head;

    //loop to handle filling the linked list
    for (i = 2; i <= argc - 1; ++i) {

        current -> data = atoi(argv[i]);
        current -> link = NULL;

        //once we get to argc - 2 we want to jump out to stop creating extra unused nodes
        if (i <= argc - 2) {
            current -> link = malloc(sizeof(Node));
            current = current -> link;
        }
        
    }
    //print list and free memory
    printList(head);
    free(head);
    return 0;

}

//function to print data from the linked list
void printList(Node *head) {
    if(head == NULL) {
        printf("No dice");
    }
    Node *ptr = head;
    while (ptr != NULL) {
        printf("%d\n", ptr -> data);
        ptr = ptr -> link;
    }
}