class Solution:
    def sortArrayByParityII(self, A):
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
        A[::2] = evenlist
        A[1::2] = oddlist
        return A


if __name__ == '__main__':
    print(Solution().sortArrayByParityII([3, 1, 2, 4]))
