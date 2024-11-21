#include <stdio.h>
#include <stdlib.h>
//type creation
typedef struct Node Node;

// node structure declaration
struct Node {
    int data;
    Node *prev;
    Node *next;
};
Node* fillNode(int length, char *argv[]);
void sortList(Node *first);
void findDuplicates(Node *first);
void printUnique(Node *first);
void deleteNode( Node** first, int item);

int main( int argc, char *argv[]) {


    int length = argc - 1;
    int flag = 0;
    int arr[length];
    
    for (int i = 1; i <= length; i++) {
        for (int j = i + 1; j < length; j++) {
            if (argv[i] == argv[j]) {
                break;
            }
        }
        if (flag == 1) {
            arr[i] = atoi(argv[i]);
        }
        printf("%d\n", arr[i]);
    }
}

Node* fillNode(int length, char *argv[]) {
    Node *first = NULL;
    Node *current = NULL;
    Node *prev = NULL;

    first = (Node*)calloc(1, sizeof(Node));
    current = first;

    //fill nodes with data
    for(int i = 0; i < length; ++i) {
        current->data = atoi(argv[i + 1]);

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

    return first;
}