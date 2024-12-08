#include <stdio.h>
#include <stdlib.h>
int main()
{
    FILE *fp=NULL;
    char ch;
    fp = fopen("abc.txt", "a+");

    if(fp == NULL)
    {
        printf("No file");
        exit(1);
    }
    fputs("this is awesome", fp);
    rewind(fp);

    while(!feof(fp))
    {
        ch = fgetc(fp);
        printf("%c", ch);
    }
    return 0;
}