#include <stdio.h>
#include <stdlib.h>


int main(int arc, char*argv[])


{

  int my_height;
  int your_height;

  my_height = atoi(argv[1]);
  your_height = atoi(argv[2]);

  if (your_height > my_height) {
    printf("You are taller than me.\n");
  }

  if (your_height < my_height) {
    printf("I am taller than you.\n");
  }

  if (your_height == my_height) {
    printf("We are exactly the same height.\n");
  }

  return 0;

}
