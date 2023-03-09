#include <stdio.h>
#include <stdlib.h>
#define PI 3.1415

int main(int argc, char*argv[])
{

  if (argc == 1) {
    printf("No input given!\n");
    return 0;
  }

  if (argc == 2) {
    printf("Two arguments needed!\n");
    return 0;
  }
  int radius = atoi(argv[1]);
  int height = atoi(argv[2]);

  if (radius < 0 || height < 0) {
    printf("The radious or height cannot be negative!\n");
    return 0;
  }

  float area = (2*PI*radius*height) + (2*PI*(radius*radius));

  printf("%.2f\n", area);

  return 0;
}
