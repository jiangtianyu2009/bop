class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        retval = False
        swaplist = []

        if len(A) == len(B):
            strindex = 0
            while strindex < len(A):
                if A[strindex] != B[strindex]:
                    swaplist.append(strindex)
                strindex = strindex + 1
        if len(swaplist) == 2:
            if A[swaplist[0]] == B[swaplist[1]]:
                if A[swaplist[1]] == B[swaplist[0]]:
                    retval = True
        if len(swaplist) == 0:
            strindex = 0
            while strindex < len(A):
                if A[strindex] in A[0:strindex]:
                    retval = True
                strindex = strindex + 1
        return retval


if __name__ == '__main__':
    print(Solution().buddyStrings("ab", "ab"))
