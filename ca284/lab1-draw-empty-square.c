#include <stdio.h>
#include <stdlib.h>


int main(int argc, char*argv[])
{

  int size = atoi(argv[1]);

  for (int i = 0; i < size; i++)
  {
    printf("*");
  }

  printf("\n");

  for (int i = 0; i < size - 2; i++)
  {

    for (int j = 0; j < size; ++j)
    {
      if (j == 0)
      {
        printf("*");
      }
      else if (j == size - 1)
      {
        printf("*");
      }

      else
      {
        printf(" ");
      }
    }
    printf("\n");

  }

  for (int i = 0; i < size; i++)
  {
    printf("*");
  }

  printf("\n");
  return 0;
}
