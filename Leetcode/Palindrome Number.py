'''
Leetcode

9. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.
'''


def equalreverse(p):
    """
    :type x: int
    :rtype: bool
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

    if y == p:
        return True
    else:
        return False


if __name__ == '__main__':
    print(equalreverse(-2147447412))
