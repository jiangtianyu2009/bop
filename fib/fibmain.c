#include <stdio.h>
#include <stdlib.h>

int fib1(int n)
{
	if (n == 0)
		return 0;
	if (n == 1)
		return 1;
	else
		return fib1(n - 1) + fib1(n - 2);
}

int fib2(int n)
{
	int a = 1;
	int b = 1;
	int c = 2;
	if (n == 0)
		return 0;
	if (n == 1)
		return 1;
	if (n == 2)
		return 1;
	else
	{
		for (int i = 0; i < n - 3; i++)
		{
			a = b;
			b = c;
			c = a + b;
		}
		return c;
	}
}

int main()
{
	int count = 35;
	for (int i = 1; i < count; i++)
		printf("%d ", fib1(i));
	printf("\n");
	for (int i = 1; i < count; i++)
		printf("%d ", fib2(i));
	printf("\n");
	return 0;
}