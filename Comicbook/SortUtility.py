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

    def quickSort(self, unsortedlist):
        if len(unsortedlist) <= 1:
            return unsortedlist
        pivotIndex = random.randint(0, len(unsortedlist) - 1)
        pivot = unsortedlist[pivotIndex]
        unsortedlist.remove(unsortedlist[pivotIndex])
        left, right = [], []
        for num in unsortedlist:
            if num < pivot:
                left.append(num)
            else:
                right.append(num)
        return self.quickSort(left) + [pivot] + self.quickSort(right)
