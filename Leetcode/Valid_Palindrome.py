class Solution:
    def isPalindrome(self, s):
        if s is None:
            return True
        lowerStr = s.lower()
        print(lowerStr)
        charList = []
        for char in lowerStr:
            if char.isalnum():
                charList.append(char)
        print(charList)
        return charList == charList[::-1]


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    m = "0P"
    Solution().isPalindrome(m)
