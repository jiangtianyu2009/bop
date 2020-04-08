#include <stdio.h>
#include <math.h>

int gcd(int x, int y)
{
	if (x < y)
		return gcd(y, x);
	if (y == 0)
		return x;
	else
		return gcd(x - y, y);
}

int main()
{
	int a = 3;
	int b = 3;
	int counta = 0;
	int countb = 0;
	int tmpa = a;
	int tmpb = b;
	while (tmpa)
	{
		tmpa /= 10;
		counta++;
	}
	while (tmpb)
	{
		tmpb /= 10;
		countb++;
	}
	int fractions = a * (pow(10, countb) - 1) + b;
	int numerator = (pow(10, countb) - 1) * pow(10, counta);
	int gcdnum = gcd(fractions, numerator);
	printf("%d / %d\n", fractions / gcdnum, numerator / gcdnum);
	return 0;
}