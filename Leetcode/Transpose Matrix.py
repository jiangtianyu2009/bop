class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        retnum = len(A[0])
        counter = 0
        outlist = []
        while counter < retnum:
            childoutlist = []
            for childlist in A:
                childoutlist.append(childlist[counter])
            counter = counter + 1
            outlist.append(childoutlist)
        return outlist


if __name__ == '__main__':
    print(Solution().transpose([[1, 2, 3], [4, 5, 6]]))
