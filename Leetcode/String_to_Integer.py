class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        int_list = []
        is_start = False
        is_minus = False
        for char in str:
            if char == ' ':
                if is_start:
                    break
                else:
                    pass
            elif char == '-':
                if is_start:
                    break
                else:
                    is_minus = True
                    is_start = True
            elif char == '+':
                if is_start:
                    break
                else:
                    is_start = True
            elif ('0' <= char <= '9'):
                is_start = True
                int_list.append(int(char))
            else:
                break
        print(int_list)
        value = 0
        for i, num in enumerate(int_list):
            value = value + num * (10 ** (len(int_list) - i - 1))
        if is_minus is True:
            value = -value
        if value > INT_MAX:
            return INT_MAX
        elif value < INT_MIN:
            return INT_MIN
        else:
            return value


if __name__ == "__main__":
    assert Solution().myAtoi("42") == 42
    assert Solution().myAtoi("   -42") == -42
    assert Solution().myAtoi("4193 with words") == 4193
    assert Solution().myAtoi("words and 987") == 0
    assert Solution().myAtoi("-91283472332") == -2147483648
    assert Solution().myAtoi("4193withwords") == 4193
    assert Solution().myAtoi("3.14159") == 3
    assert Solution().myAtoi(".1") == 0
    assert Solution().myAtoi("-+1") == 0
    assert Solution().myAtoi(" b11228552307") == 0
    assert Solution().myAtoi("+1") == 1
