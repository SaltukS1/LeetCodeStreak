from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board: List[List[str]], row: int, col: int) -> bool:
            # Check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check upper left diagonal
            for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            # Check upper right diagonal
            for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        
        def backtrack(board: List[List[str]], row: int):
            if row == n:
                # Convert board to required format
                result.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row + 1)
                    board[row][col] = '.'
        
        # Initialize empty board
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        backtrack(board, 0)
        return result

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print("Solutions for n=4:")
    for solution in sol.solveNQueens(4):
        print("\n".join(solution))
        print()
    
    print("Number of solutions for n=8:", len(sol.solveNQueens(8))) 