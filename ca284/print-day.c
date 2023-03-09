#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{

  char *week[] = {"Empty", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

  int number = atoi(argv[1]);
  char *day = week[number];
  printf("%s\n", day);
  return 0;
}
