/*
Author: Senan Warnock

Description: This program takes command line arguments and creates a data structure array of the information,
then prints out any country that has a size smaller than 100,000 km2

Date 30th of October

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// define CountryInfo type.
typedef struct CountryInfo CountryInfo;

void printData(CountryInfo *arr, int count);

//CountryInfo definition
struct CountryInfo
{
    char name[20];
    char capital[20];
    float population;
    int size;
};

int main(int argc, char *argv[]) {

    //initialize struct.
    CountryInfo countryData[50];
    int i;
    int count = 0;
    int j = 1;
    int leng = argc - 1;

    //copy command line args into struct.
    while (j < leng) {

        strcpy(countryData[count].name, argv[j]);
        j++;
        strcpy(countryData[count].capital, argv[j]);
        j++;
        countryData[count].population = atof(argv[j]);
        j++;
        countryData[count].size = atoi(argv[j]);
        count++;
        j++;

    }

    //print headings.
    printf("Country\t\t\tCapital\t\t\tSize\t\t\tPopulation\n");
    

    //print data
    printData(countryData, count);

    return 0;
}


//function to print data of each country if the size is smaller than 100,000
void printData(CountryInfo *arr, int count) {
    
    int i;

    for (i = 0; i < count; i++) {
        if (arr[i].size < 100000) {
            printf("%s\t\t\t%s\t\t\t%d\t\t\t%.2f\n", arr[i].name, arr[i].capital, arr[i].size, arr[i].population);
        }
    }

}

