from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row_list = []
        zero_col_list = []
        for i, row in enumerate(matrix):
            for j, column in enumerate(row):
                if column == 0:
                    zero_col_list.append(j)
                    zero_row_list.append(i)
        for i, row in enumerate(matrix):
            for j, column in enumerate(row):
                if j in zero_col_list:
                    matrix[i][j] = 0
                if i in zero_row_list:
                    matrix[i][j] = 0
        print(zero_row_list)
        print(zero_col_list)
        print(matrix)


if __name__ == "__main__":
    Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
