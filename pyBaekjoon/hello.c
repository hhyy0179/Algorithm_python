#include <stdio.h>

int main(void)
{

    char a = 'a';
    void* a_ptr = &a;
    void** ptr = &a_ptr;
    char* name = (char*) *ptr;
    printf("%s", name);

    void** ptr2 = ptr;
    int64_t* number = (int64_t*) *ptr2;
    printf("%lld", *number);

    // void** ptr2 = 0x00000000FFFF3821; // 마찬가지
    // int64_t* number = (int64_t*) *ptr2;
    // printf("%p", *number);


    return 0;
}