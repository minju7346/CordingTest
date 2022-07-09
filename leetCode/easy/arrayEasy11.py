from copy import deepcopy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        tmp, n = deepcopy(matrix), len(matrix)
        for r in range(n):
            for c in range(n):
                matrix[r][c] = tmp[n - 1 - c][r]

