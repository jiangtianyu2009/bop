#include <stdio.h>

void reverseString(char *s, int sSize);

int main(void)
{
    char str[] = "Hello";
    reverseString(str, sizeof(str) - 1);
    printf("%s", str);
    return 0;
}

void reverseString(char *s, int sSize)
{
    char tmp;
    for (int i = 0; i < sSize / 2; i++)
    {
        tmp = *s;
        *(s + sSize) = *s;
        *(s + sSize) = tmp;
        s++;
        sSize--;
    }
}