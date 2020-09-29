from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_list = []
        ret_list = []
        ret_dict = {}
        dict_dict = {}
        for word in strs:
            dict_new = {}
            for char in word:
                if char not in dict_new.keys():
                    dict_new[char] = 1
                else:
                    dict_new[char] = dict_new[char] + 1
            if dict_new not in dict_list:
                dict_list.append(dict_new)
        print(dict_list)
        for i in range(len(dict_list)):
            dict_dict[i] = dict_list[i]
            ret_dict[i] = []
        print(dict_dict)
        print(ret_dict)
        for word in strs:
            dict_new = {}
            for char in word:
                if char not in dict_new.keys():
                    dict_new[char] = 1
                else:
                    dict_new[char] = dict_new[char] + 1
            for i in range(len(dict_list)):
                if dict_dict[i] == dict_new:
                    ret_dict[i].append(word)
        print(ret_dict)
        for i in range(len(dict_list)):
            ret_list.append(ret_dict[i])
        print(ret_list)
        return ret_list


if __name__ == "__main__":
    assert {"a": 1, "b": 1} == {"b": 1, "a": 1}  # Test dict order
    assert Solution().groupAnagrams(["ddddddddddg", "dgggggggggg"]) \
        == [['ddddddddddg'], ['dgggggggggg']]
    assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) \
        == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert Solution().groupAnagrams([""]) == [[""]]
    assert Solution().groupAnagrams(["a"]) == [["a"]]
