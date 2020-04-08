#include <stdio.h>

void findTango(int * tid, int num)
{
	int tmp = 0;
	int count = 0;
	for (int i = 0; i < num; i++)
	{
		if (count == 0)
		{
			tmp = tid[i];
			count++;
		}
		else if (tid[i] == tmp)
			count++;
		else
			count--;
	}
	printf("%d\n", tmp);
}

int main()
{
	int tid1[10] = { 1, 2, 3, 4, 4, 4, 4, 4, 4, 5 };
	int tid2[10] = { 4, 2, 4, 4, 1, 4, 3, 5, 4, 4 };
	findTango(tid1, 10);
	findTango(tid2, 10);
	return 0;
}