# Staircase search - time: O(m + n) space: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])  # m rows, n cols
        r, c = 0, n - 1

        while r < m and c >= 0:
            if target < matrix[r][c]:
                c -= 1
            elif target > matrix[r][c]:
                r += 1
            else:
                return True

        return False
