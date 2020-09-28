class Solution:
    def threeSum(self,  nums):
        if len(nums) < 3:
            return []
        if self.is_all_zero(nums):
            return [[0, 0, 0]]
        retList = []
        nums = sorted(nums)
        for index, num in enumerate(nums):
            retList = retList + self.twoSumPro(nums[index + 1:], -num)
        return self.deDup(sorted(retList))

    def twoSumPro(self, nums, target):
        numDict = {}
        retList = []
        for index, num in enumerate(nums):
            if (target - num) not in numDict:
                numDict[num] = index
            else:
                retList.append(sorted([target - num, num, -target]))
        return self.deDup(retList)

    def deDup(self, ret_list):
        dedup_list = []
        for i, nums in enumerate(ret_list):
            if i != 0 and ret_list[i] == base_nums:
                pass
            else:
                base_nums = nums
                dedup_list.append(nums)
        return dedup_list

    def is_all_zero(self, nums):
        zero_flag = True
        for num in nums:
            if num == 0:
                pass
            else:
                zero_flag = False
        return zero_flag


if __name__ == '__main__':
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]
                               ) == [[-1, -1, 2], [-1, 0, 1]]
    assert Solution().threeSum([0, 0, 0, 0, 0, 0, 0]) == [[0, 0, 0]]
