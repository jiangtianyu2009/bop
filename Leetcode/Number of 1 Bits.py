class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n is not 0:
            cnt = cnt + n % 2
            n = n >> 1
        return cnt
