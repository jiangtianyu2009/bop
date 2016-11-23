#include <stdio.h>
#include <stdlib.h>

void findMaxK(int * array, int length, int k)
{
	int minofKindex = 0;
	int minofK = 0;
	int * p = malloc(sizeof(int) * k);
	for (int i = 0; i < k; i++)
		*(p + i) = 0;
	for (int m = 0; m < length; m++)
	{
		minofK = *p;
		minofKindex = 0;
		for (int i = 0; i < k; i++)
			if (minofK > *(p + i))
			{
				minofKindex = i;
				minofK = *(p + i);
			}
		if (*(array + m) > *(p + minofKindex))
			*(p + minofKindex) = *(array + m);
		for (int i = 0; i < k; i++)
			printf("%d ", *(p + i));
		printf("\n");
	}
	printf("\n");
	printf("\n");
	printf("\n");
	free(p);
}

int main()
{
	int array[10] = { 5, 4, 6, 2, 1, 7, 9, 8, 3, 0 };
	for (int i = 3; i < 8; i++)
	{
		printf("max %d num:\n", i);
		findMaxK(array, 10, i);
	}
	return 0;
}