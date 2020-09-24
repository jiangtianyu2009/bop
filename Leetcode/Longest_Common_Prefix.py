from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        commstr = ""
        if len(strs) == 0:
            return commstr
        len_min = len(strs[0]) if len(strs[0]) < len(
            strs[-1]) else len(strs[-1])
        for i in range(0, len_min):
            if strs[0][i] == strs[-1][i]:
                commstr = commstr + strs[0][i]
            else:
                break
        print(commstr)
        return commstr


if __name__ == "__main__":
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert Solution().longestCommonPrefix([]) == ""
