class Sort:
    def __init__(self):
        pass

    def bubbleSort(self, nums):
        sortedlength = 0
        for k, num in enumerate(nums[:len(nums) - sortedlength]):
            sortedlength = k + 1
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
        pass
