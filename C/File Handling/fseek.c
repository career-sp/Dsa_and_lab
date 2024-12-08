#include <stdio.h>
#include <stdlib.h>
int main()
{
    FILE *fp = NULL;
    fp = fopen("abc.txt", "r");
    if(fp == NULL)
    {
        printf("Cannot open");
        exit(1);
    }

    fseek(fp, 6, SEEK_SET);

    return 0;
}