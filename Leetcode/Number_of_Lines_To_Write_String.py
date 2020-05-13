class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        Line = 0
        SUM = 0
        for x in S:
            CH = widths[ord(x) - 97]
            SUM += CH
            if SUM > 100:
                Line += 1
                SUM = CH
        return [Line+1, SUM]
