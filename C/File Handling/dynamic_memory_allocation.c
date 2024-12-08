// taking user inputs dynamically.

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    printf("Enter the values : ");
    scanf("%d", &n);

    int *ptr;
    ptr = (int*) malloc(n * sizeof(int));

    printf("Enter the values : ");
    for(int i=0; i<n; i++)
    {
        scanf("%d", (ptr+i));
    }

    printf("\nThe values are : ");
    for(int i=0; i<n; i++)
    {
        printf(" %d ", *(ptr+i));
    }
    return 0;
}