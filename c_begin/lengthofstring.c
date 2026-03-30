#include<stdio.h>
int main()
{
    char a[] = "String";
    int length = 0;
    for(int i=0;a[i]!='\o';i++){
        length++;
    }
    printf("Length of the string is %d",length);
    return 0;
}