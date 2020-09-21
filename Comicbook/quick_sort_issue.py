import random


class Sort:
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


if __name__ == "__main__":
    a = [76, 76, 65, 72, 58, 64, 82, 3, 22, 31]
    print(Sort().quickSort(a))
    print(Sort().quickSort(a))
    print(Sort().quickSort(a))
    print(Sort().quickSort(a))
