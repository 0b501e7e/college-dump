#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{

  int values[argc];
  int odd = 0;
  int i = 0;


  for (i = 1; i < argc; i++)
  {

    values[i] = atoi(argv[i]);
  }

  for (i = 0; i < argc; i++)
  {

     if (values[i] % 2 != 0)
       odd++;
  }

  printf("%d\n", odd);
  return 0;
}
