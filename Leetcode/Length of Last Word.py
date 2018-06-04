class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        for char in s:
            if char is ' ':
                counter = 0
            else:
                counter = counter + 1
        return counter


if __name__ == '__main__':
    print(Solution().lengthOfLastWord('a'))
