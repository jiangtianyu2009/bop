class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        out = False
        if rec2[0] >= rec1[2] or rec2[1] > rec1[3]:
            out = True
        if rec1[0] >= rec2[2] or rec1[1] > rec2[3]:
            out = True
        return not out
