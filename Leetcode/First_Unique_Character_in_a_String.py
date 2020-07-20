from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_char = {}
        for char in s:
