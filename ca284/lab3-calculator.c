#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char*argv[])
{
	char mult[] = "multiply";
	char div[] = "divide";
	char zero[] = "0";
	float num1 = atof(argv[2]);
	float num2 = atof(argv[3]);


	if (strcmp(argv[2], zero) == 0 || strcmp(argv[3], zero) == 0 && (strcmp(argv[1], div) == 0)) {
		printf("invalid\n");
		return 0;
	}

	else if (strcmp(argv[1], mult) == 0) {
		float answer = num1 * num2;
		printf("%f\n", answer);
		return 0;
	}

	else if (strcmp(argv[1], div) == 0) {
		float answer = num1 / num2;
		printf("%f\n", answer);
		return 0;
	}

}