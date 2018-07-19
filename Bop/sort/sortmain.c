#include <stdio.h>
#include <stdlib.h>

void printResult(int array[], int n, char* s)
{
	printf("%s", s);
	for (int i = 0; i < n; i++)
		printf("%d ", array[i]);
	printf("\n\n");
}

void insertSort(int array[], int n)
{
	int k = 0;
	for (int i = 1; i < n; i++)
	{
		int tmp = array[i];
		for (k = i; k > 0 && array[k - 1] > tmp; k--)
			array[k] = array[k - 1];
		array[k] = tmp;
	}
	printResult(array, n, "Result of insert sort: ");
}

void selectSort(int array[], int n)
{
	int k; int min; int minIndex;
	for (int i = 0; i < n; i++)
	{
		k = i;
		min = array[k];
		minIndex = k;
		while (k < n)
		{
			if (array[k] < min)
				minIndex = k;
			k++;
		}
		if (minIndex != i)
		{
			int tmp = array[i];
			array[i] = array[minIndex];
			array[minIndex] = tmp;
		}
	}
	printResult(array, n, "Result of select sort: ");
}

void bubbleSort(int array[], int n)
{
	for (int i = 0; i < n; i++)
	{
		for (int k = 0; k < n - i - 1; k++)
		{
			if (array[k] > array[k + 1])
			{
				int tmp = array[k];
				array[k] = array[k + 1];
				array[k + 1] = tmp;
			}
		}
	}
	printResult(array, n, "Result of bubble sort: ");
}

void shelldSort(int array[], int n)
{

}

void merge(int array1[], int array2[], int m, int n)
{
	int * array = malloc(sizeof(int) * (m + n));
	int * resultArray = array;
	int mcount = m;
	int ncount = n;
	while (m || n)
	{
		if ((*array1 < *array2) && (m > 0))
		{
			*array = *array1;
			array1++;
			m--;
		}
		else if (n > 0)
		{
			*array = *array2;
			array2++;
			n--;
		}
		array++;
	}
	array = resultArray;
	m = mcount;
	n = ncount;
}

void mergedSort(int array[], int argn)
{
	int m = argn / 2;
	int n = argn - m;
	if ((m == 1) && (n == 1))
		merge(array, array + m, m, n);
	else if (m == 1)
	{
		mergedSort(array + m, n);
		merge(array, array + m, m, n);
	}
	else if (n == 1)
	{
		mergedSort(array, m);
		merge(array, array + m, m, n);
	}
	else
	{
		mergedSort(array, m);
		mergedSort(array + m, n);
		merge(array, array + m, m, n);
	}
	printResult(array, argn, "Result of merged sort: ");
}

int main()
{
	int num = 12;
	int inputArray[12] = { 3, 20, 4, 7, 1, 43, 12, 88, 5, 7, 101, 62 };
	printf("Input array is 3, 20, 4, 7, 1, 43, 12, 88, 5, 7, 101, 62.\n\n");
	insertSort(inputArray, num);
	selectSort(inputArray, num);
	bubbleSort(inputArray, num);
	mergedSort(inputArray, num);

	return 0;
}

