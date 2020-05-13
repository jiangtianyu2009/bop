class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        out = []
        for subA in A:
            outA = Solution.revList(self, subA[::-1])
            out.append(outA)
        return out

    def revList(self, subA):
        lsA = []
        for char in subA:
            if char == 1:
                outch = 0
            else:
                outch = 1
            lsA.append(outch)
        return lsA
