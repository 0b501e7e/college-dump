#include<stdio.h>

void swap_with_pointer(int *a, int *b);

int main(int argc, char *argv[])
{
	int num1 = 5;
	int num2 = 6;

	int *pNum1 = NULL; /* initialise a pointer with NULL, i.e, a pointer to nothing */
	int *pNum2 = 0; /* Another way of intitialise a pointer to nothing (NULL) */

	printf("Before swap : num1 = %d, num2 = %d \n", num1, num2);

	pNum1 = &num1;
	pNum2 = &num2;

	swap_with_pointer(pNum1,pNum2);
	printf("After swap : num1 = %d, num2 = %d \n", num1, num2);

	return 0;
}

void swap_with_pointer(int *a, int *b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}