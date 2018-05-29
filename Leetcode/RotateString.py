class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        output = False
        doubleA = A + A
        if B in doubleA and len(B) == len(A):
            output = True
        return output
