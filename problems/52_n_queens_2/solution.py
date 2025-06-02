class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_safe(row: int, col: int, queens: list[int]) -> bool:
            # Check if placing a queen at (row, col) is safe
            for r in range(row):
                # Check same column
                if queens[r] == col:
                    return False
                # Check diagonals
                if abs(queens[r] - col) == abs(r - row):
                    return False
            return True

        def backtrack(row: int, queens: list[int], count: int) -> int:
            # If we've placed n queens, we found a solution
            if row == n:
                return count + 1

            # Try placing queen in each column of current row
            for col in range(n):
                if is_safe(row, col, queens):
                    queens[row] = col
                    count = backtrack(row + 1, queens, count)
                    queens[row] = -1  # Backtrack

            return count

        # Initialize queens array with -1 (no queen placed)
        queens = [-1] * n
        return backtrack(0, queens, 0)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: n = 4
    print(f"n = 4: {solution.totalNQueens(4)}")  # Expected output: 2
    
    # Test case 2: n = 1
    print(f"n = 1: {solution.totalNQueens(1)}")  # Expected output: 1
    
    # Test case 3: n = 2
    print(f"n = 2: {solution.totalNQueens(2)}")  # Expected output: 0 