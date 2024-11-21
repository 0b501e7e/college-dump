/*
Author: Senan Warnock

Date: 25th of November

Description:

This program takes command line arguments and creates a linked list of the data.
Then if the price of a product is from Ireland, it updates the pricre by 20%
and prints the items in the list.
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//type definition of Product
typedef struct Product Product;

//function prototypes
void printList(Product *head);
void updatePrice(Product *head);
void delete(Product *head);
int countNodes(Product *head);

//struct definition
struct Product {

    char *code;
    char *origin;
    int price;
    Product *next;
    

};

int main(int argc, char *argv[]) {

    int i = 1;
    
    Product *current, *first;
    //create first node
    first = calloc(1, sizeof(Product));
    current = first;

    //assign data to nodes
    while(i < argc - 1) {

        current->code = argv[i];
        i++;
        current->origin = argv[i];
        i++;
        current->price = atoi(argv[i]);
        i++;
        current->next = calloc( 1, sizeof(Product));
        current = current->next;
    }
    //delete extra node
    delete(first);

    //update prices
    updatePrice(first);

    //print list
    printList(first);


    return 0;


}

//function to update price
void updatePrice(Product *head) {

    //pointer to head
    Product *ptr = head;

    //traverse the list and if we see the origin is Ireland, update the price by 20%
    while (ptr->next != NULL) {
        
        //list is empty
        if (ptr == NULL) {
            return;
        }
        
        //if origin is Ireland update the price
        else if (strcmp(ptr->origin, "Ireland") == 0) {

            ptr->price += ptr->price * 0.2;
            ptr = ptr->next;
        }
        //traverse
        else {
            ptr = ptr->next;
        }
    }
}

//function to print the list
void printList(Product *head) {
	
    //pointer to head
    Product *p = head;
    
    //traverse the list and print the data
	while (p != NULL) {
		printf("%s\n%s\n%d\n", p->code, p->origin, p->price);
        p = p->next;
	}
}

//function to delete the last node
void delete(Product *head) {
    //pointers to head
    Product *ptr = head, *prev = ptr;

    //traverse the list till the end
    while (ptr->next != NULL) {
        prev = ptr;
        ptr = ptr->next;
    }
    //delete
    prev->next = NULL;
    free(ptr);
    ptr = NULL;
}