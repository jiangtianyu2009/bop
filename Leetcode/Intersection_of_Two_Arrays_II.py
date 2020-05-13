from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        index_1 = 0
        index_2 = 0
        print(nums1)
        print(nums2)
        while(index_1 < len(nums1)):
            while(index_2 < len(nums2)):
                print(index_1)
                print(index_2)
                if(nums1[index_1] == nums2[index_2]):
                    res.append(nums1[index_1])
                    print(nums1)
                    print(nums2)
                    nums1[index_1] = 0
                    nums2[index_2] = 0
                index_2 = index_2 + 1
            index_1 = index_1 + 1
        return res


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2]
    print(Solution().intersect(nums1, nums2))
