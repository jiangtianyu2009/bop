class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counter = 0
        for schar in S:
            for jchar in J:
                if jchar == schar:
                    counter = counter + 1
        return counter
