#include <stdio.h>

void reverseString(char *s, int sSize);

int main(void)
{
    char str[] = {'A',' ','m','a','n',',',' ','a',' ','p','l','a','n',',',' ','a',' ','c','a','n','a','l',':',' ','P','a','n','a','m','a'};
    reverseString(str, sizeof(str));
    printf("%s", str);
    return 0;
}

void reverseString(char *s, int sSize)
{
    char tmp;
    for (int i = 0; i <= sSize / 2; i++)
    {
        tmp = *s;
        *s = *(s + sSize);
        *(s + sSize) = tmp;
        s++;
        sSize--;
        sSize--;
    }
}