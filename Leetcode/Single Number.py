class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        resum = 0
        index = 0
        for num in nums:
            resum = resum ^ num
            index = index + 1
        return resum


if __name__ == '__main__':
    print(Solution().singleNumber(
        [17, 12, 5, -6, 12, 4, 17, -5, 2, -3, 2, 4, 5, 16, -3, -4, 15, 15, -4, -5, -6]))
