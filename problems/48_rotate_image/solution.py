from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose the matrix (swap (i,j) with (j,i) for i < j)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row (to rotate clockwise)
        for i in range(n):
            matrix[i].reverse()

# Test cases
if __name__ == "__main__":
    sol = Solution()
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix1)
    print(matrix1)  # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(matrix2)
    print(matrix2)  # Expected: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]] 