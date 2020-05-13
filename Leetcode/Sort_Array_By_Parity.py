class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        oddlist = []
        evenlist = []
        for elem in A:
            if elem % 2 == 0:
                evenlist.append(elem)
            else:
                oddlist.append(elem)
        return evenlist + oddlist


if __name__ == '__main__':
    print(Solution().sortArrayByParity([3, 1, 2, 4]))
