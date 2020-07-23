class Solution:
    def twoSum(self, nums, target):
        numDict = {}
        for index, num in enumerate(nums):
            if (target - num) not in numDict:
                numDict[num] = index
            else:
                return numDict[target - num], index
        return 0, 0


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
