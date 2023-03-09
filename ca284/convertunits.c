#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{

  int centimetres;
  float inches;
  float divisor = 2.54;

  centimetres = atoi(argv[1]);

  inches = centimetres / divisor;

  printf("You have %f inches \n", inches);

}
