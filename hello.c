#include <stdio.h>

int main(void)
{
    
    int a = 0x1C;
    int *b = a;
    int c;
    scanf("%d",&c);
    printf("%p\n",&c);
    printf("%p\n",b);

    return 0; 
}