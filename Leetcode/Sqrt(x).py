class Solution:
    def mySqrt(self, x: int) -> int:
        aim = x
        while int(x / 2) * int(x / 2) > aim:
            x = int(x / 2)
        search_space = [int(x / 2), x]
        print(search_space)
        if search_space[0] * search_space[0] == aim:
            return search_space[0]
        if search_space[1] * search_space[1] == aim:
            return search_space[1]
        while search_space[0] * search_space[0] <= aim:
            search_space[0] = search_space[0] + 1
        return search_space[0] - 1


if __name__ == "__main__":
    assert Solution().mySqrt(8) == 2
    assert Solution().mySqrt(1) == 1
