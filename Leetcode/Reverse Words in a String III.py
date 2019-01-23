class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        restr = []
        slist = s.split()
        for sl in slist:
            restr.append(sl[::-1])
        return ' '.join(restr)


if __name__ == '__main__':
    print(Solution().reverseWords("Let's take LeetCode contest"))
