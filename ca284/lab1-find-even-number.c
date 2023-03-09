#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{

  int values[argc];
  int i = 0;
  int empty = 0;

  for (i = 1; i < argc; i++)
  {

    values[i] = atoi(argv[i]);
  }

  for (i = 1; i < argc; i++)
  {

     if (values[i] % 2 == 0)
     {
       printf("%d - %d\n", (i - 1), values[i]);
       empty++;
     }

  }

  if (empty == 0)
  {
    printf("Not found!\n");
  }

  return 0;
}

