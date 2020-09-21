import random


class Sort:
    def __init__(self):
        pass

    def bubbleSort(self, nums):
        for n in nums:
            for i, num in enumerate(nums):
                if i == 0:
                    pass
                else:
                    if nums[i] < nums[i - 1]:
                        nums[i] = nums[i] + nums[i - 1]
                        nums[i - 1] = nums[i] - nums[i - 1]
                        nums[i] = nums[i] - nums[i - 1]
        return nums

    def quickSort(self, nums):
        nums = nums[:]
        if len(nums) <= 1:
            return nums
        pivot = nums[random.randint(0, len(nums) - 1)]
        nums.remove(pivot)
        left, right = [], []
        for num in nums:
            if num < pivot:
                left.append(num)
            else:
                right.append(num)
        return self.quickSort(left) + [pivot] + self.quickSort(right)
