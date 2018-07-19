class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zerocounter = 0
        for num in nums:
            if num is 0:
                zerocounter = zerocounter + 1
        deltalens = zerocounter
        while zerocounter is not 0:
            nums.remove(0)
            zerocounter = zerocounter - 1
        while deltalens is not 0:
            nums.append(0)
            deltalens = deltalens - 1


if __name__ == '__main__':
    nums = [0, 0, 1]
    Solution().moveZeroes(nums)
    print(nums)
