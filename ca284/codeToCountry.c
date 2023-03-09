#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{
  int countryCode;
  countryCode = atoi(argv[1]);

  switch(countryCode)
  {
    case 353:
      printf("Ireland\n");
      break;
    case 44:
      printf("UK\n");
      break;
    case 33:
      printf("France\n");
      break;
    case 34:
      printf("Spain\n");
      break;
    default:
      printf("Undefined!\n");
      break;
  }

  return 0;

}
