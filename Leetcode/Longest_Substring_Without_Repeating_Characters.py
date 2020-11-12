class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_array = []
        res_list = []
        for i, char in enumerate(s):
            if char in res_list:
                res_array.append(res_list)
                res_list = res_list[res_list.index(char) + 1:]
            res_list.append(char)
        res_array.append(res_list)
        res_l_len = []
        for res_l in res_array:
            res_l_len.append(len(res_l))
        return max(res_l_len)


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("dvdf") == 3
