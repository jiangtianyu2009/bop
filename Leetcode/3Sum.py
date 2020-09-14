class Solution:
    def threeSum(self,  nums):
        temp_list = []
        nums = sorted(nums)
        for index, num in enumerate(nums):
            if nums[index + 1] == nums[index]:
                break
            target = 0 - num
            two_nums = nums[index + 1:]
            numDict = {}
            for index, two_num in enumerate(two_nums):
                if (target - two_num) not in numDict:
                    numDict[two_num] = index
                else:
                    temp_list.append([num, target - two_num, two_nums[index]])
        temp_set = set(tuple(s) for s in temp_list)
        new_list = [list(t) for t in temp_set]
        print(new_list)
        return new_list


if __name__ == '__main__':
    nums1 = [-1, 0, 1, 2, -1, -4]
    nums2 = [0, -4, -1, -4, -2, -3, 2]
    Solution().threeSum(nums2)
