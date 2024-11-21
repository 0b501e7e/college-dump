/*
Author: Senan Warnock

Description: This program takes command line input and creates a new Struct type based on the information

Date: 29th of October
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//define CountryInfo as a type
typedef struct CountryInfo CountryInfo;

//CountryInfo definition
struct CountryInfo
{
    char name[20];
    char capital[20];
    float population;
    int size;
};



int main(int argc, char *argv[]) {

    //initialize a CountryInfo data structure
    CountryInfo countryinform;

    //fill out the info for contryinform.
    strcpy(countryinform.name, argv[1]);
    strcpy(countryinform.capital, argv[2]);
    countryinform.population = atof(argv[3]);
    countryinform.size = atoi(argv[4]);

    //print the info.
    printf("%s\n%s\n%.2f million people\n%d km2\n", countryinform.name, countryinform.capital, countryinform.population, countryinform.size);

    return 0;
}