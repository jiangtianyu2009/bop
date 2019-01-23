class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        rlist = []
        for num in range(left, right + 1):
            strnum = str(num)
            numflag = True
            for char in strnum:
                if int(char) != 0:
                    if (num % int(char)) != 0:
                        numflag = False
                else:
                    numflag = False
            if numflag == True:
                rlist.append(num)
        return rlist


if __name__ == '__main__':
    print(Solution().selfDividingNumbers(1, 22))
