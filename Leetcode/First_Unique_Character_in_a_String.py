class Solution:
    def firstUniqChar(self, s):
        dict_char = {}
        for char in s:
            if char in dict_char:
                dict_char[char] += 1
            else:
                dict_char[char] = 1
        print(dict_char)
        key = self.firstUniqCharinDict(dict_char)
        index = self.getIndex(key, s)
        return index

    def firstUniqCharinDict(self, dict_char):
        for key in dict_char:
            if dict_char[key] == 1:
                print(key)
                return key
        return None

    def getIndex(self, key, s):
        if key is None:
            return -1
        else:
            index = s.index(key)
            print(index)
            return index


if __name__ == '__main__':
    s = "loveleetcode"
    Solution().firstUniqChar(s)
