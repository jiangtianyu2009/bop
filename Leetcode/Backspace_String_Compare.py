class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = []
        t = []
        for charsj in S:
            if charsj is '#':
                if len(s) is not 0:
                    s.pop()
            else:
                s.append(charsj)
        for chartj in T:
            if chartj is '#':
                if len(t) is not 0:
                    t.pop()
            else:
                t.append(chartj)
        print(s)
        print(t)
        if s == t:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().backspaceCompare("a##c", "#a#c"))
