class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        maxnum = max(A)
        return A.index(maxnum)


if __name__ == '__main__':
    print(Solution().peakIndexInMountainArray([0, 2, 1, 0]))
