'''
Leetcode

7. Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Note:
The input is assumed to be a 32-bit signed integer.
Your function should return 0 when the reversed integer overflows.
'''


def reverse(p):
    """
    :type x: int
    :rtype: int
    """
    if p > 0:
        x = p
    else:
        x = -p
    y = 0

    while x != 0:
        n = x % 10
        y = y * 10 + n
        x = x // 10

    if p > 0:
        retu = y
    else:
        retu = -y

    if retu > 2147483647 or retu < -2147483648:
        return 0
    else:
        return retu


if __name__ == '__main__':
    print(reverse(123))
