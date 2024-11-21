/*

Author: Senan Warnock
Date: 25th of November
Description: This program takes integer inputs and creates a linked list.
The program then proceeds to delete all even integers in the list, then sums
up the odd integers and pushes the result to the end of the list.

*/
#include <stdio.h>
#include <stdlib.h>

//create Node type
typedef struct Node Node;

//Node definition
struct Node {
    int data;
    Node *next;
};
//function prototypes
void printList(Node *head);
void delete(Node **head, int data);
void deleteEvens(Node **head);
void pushLast(Node **head, int data);

int main(int argc, char *argv[]) {

    int i;

    Node *head, *current, *prev;

    //create first node and point current to head
    head = malloc(sizeof(Node));
    current = head;

    //loop to handle filling the linked list
    for (i = 1; i <= argc - 1; ++i) {

        current -> data = atoi(argv[i]);
        current -> next = NULL;

        //once we get to argc - 2 we want to jump out to stop creating extra unused nodes
        if (i <= argc - 2) {
            current -> next = malloc(sizeof(Node));
            current = current -> next;
        }
        
    }

    //loop to delete all even integers in the list
    for (i = 0; i < argc - 1; i++) {
        deleteEvens(&head);
    }

    //sum the remaining odd integers and save it in sum
    int sum = 0;
    Node *ptr = head;
    while (ptr != NULL) {
        sum += ptr->data;
        ptr = ptr->next;
    }
    //push sum to the end of the list
    pushLast(&head, sum);    

    //print list
    printList(head);

    return 0;
}

//function to push last node to the list
void pushLast(Node **head, int data) {

    //create node
    Node *last = malloc(sizeof(Node));
    last->data = data;
    last->next  = NULL;

    //if list is empty set last head to last
    if (*head == NULL) {
         *head = last;
    }

    else {
        //pointer to head pointer
        Node *lastNode = *head;
        
        //traverse the list till the end
        while(lastNode->next != NULL) {
            lastNode = lastNode->next;
        }
        //add last to the list, finally!
        lastNode->next = last;
      

    }

}

//function to delete data in a node, we use this in conjunction with deleteEvens to delete the nodes we want
void delete(Node **head, int data) {

    Node *current = *head, *prev;
 
    //if the first node has data to be deleted
    if (current != NULL && current->data == data) {
        
        //create new head
        *head = current->next;

        //delete the node
        free(current);
        return;
    }
    
    //traverse the list looking for the data
    while (current != NULL && current->data != data) {
        
        prev = current;
        current = current->next;
    }
    
    //we didn't find the data
    if (current == NULL)
        
        return;
    
    //link the other nodes
    prev->next = current->next;
    
    //delete the node
    free(current);
}


//function to delete even integers in the list
void deleteEvens(Node **head) {
    
    //pointer to head pointer
    Node *ptr = *head;
 
    //traverse the list, and if data is divisible by 2, call delete function to search and delete node
    while (ptr != NULL) {

        if (ptr->data % 2 == 0)
            delete(head, ptr->data);
        ptr = ptr->next;
    }
}

//function to print the list
void printList(Node *ptr) {

    //traverse the list and print the data along the way
    while (ptr != NULL) {
        printf("%d\n", ptr->data);
        ptr = ptr->next;
    }
}

