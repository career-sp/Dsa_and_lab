#include <stdio.h>

int main()
{
    FILE *fptr1, *fptr2;
    char ch;

    fptr1 = fopen("abc.txt", "r");
    fptr2 = fopen("copy.txt", "w");

    while ((ch = fgetc(fptr1)) != EOF)
    {
        fputc(ch, fptr2);
    }

    printf("\nOperation successful");

    return 0;
}