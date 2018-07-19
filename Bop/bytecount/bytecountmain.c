#include <stdio.h>
#include <stdlib.h>

void printBinary(unsigned char v)
{
	int length = sizeof(unsigned char) * 8;
	while (length)
	{
		if ((v & 0x80) == 0x80)
			printf("1");
		else
			printf("0");
		v <<= 1;
		length--;
	}
	printf("\n");
}

void count1(unsigned char v)
{
	int num = 0;
	while (v)
	{
		if (v % 2 == 1)
			num++;
		v = v / 2;
	}
	printf("%d\n", num);
}

void count2(unsigned char v)
{
	int num = 0;
	while (v)
	{
		num += v & 0x01;
		v >>= 1;
	}
	printf("%d\n", num);
}

void count3(unsigned char v)
{
	int num = 0;
	while (v)
	{
		v &= (v - 1);
		num++;
	}
	printf("%d\n", num);
}

int main()
{
	unsigned char v = 0x00000011;
	printBinary(v);
	count1(v);
	count2(v);
	count3(v);
	return 0;
}

