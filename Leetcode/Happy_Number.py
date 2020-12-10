class Solution:
    res_array = []

    def isHappy(self, n: int) -> bool:
        self.res_array.clear()
        m = self.compute(n)
        print(m)
        if m == 1:
            return True
        elif m == 0:
            return False
        else:
            return False

    def compute(self, n: int) -> int:
        dig_array = list(str(n))
        print(dig_array)
        res = 0
        for digit in dig_array:
            res = res + int(digit) * int(digit)
        print(res)
        if res in self.res_array:
            return 0
        else:
            self.res_array.append(res)
            print(self.res_array)

            if res == 1:
                return 1
            else:
                return self.compute(res)


if __name__ == "__main__":
    assert Solution().isHappy(19) == True
    assert Solution().isHappy(2) == False
    assert Solution().isHappy(1) == True
    assert Solution().isHappy(7) == True
