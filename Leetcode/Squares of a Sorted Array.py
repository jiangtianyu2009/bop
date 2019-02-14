class Solution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        B = []
        for elem in A:
            B.append(elem * elem)
        B.sort()
        return B
