class Solution:
    def reverse(self, nums):
        start = 0
        end = len(nums) - 1
        while (start < end):
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start = start + 1
            end = end - 1
        return nums

    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if(k > len(nums)):
            k = k - len(nums)
        nums = self.reverse(nums)
        print(nums)
        nums[0:k] = self.reverse(nums[0:k])
        print(nums[0:k])
        nums[k:len(nums)] = self.reverse(nums[k:len(nums)])
        print(nums[k:len(nums)])


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    Solution().rotate(nums, 1)
    print(nums)
