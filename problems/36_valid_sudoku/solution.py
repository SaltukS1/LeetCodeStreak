from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize dictionaries to track numbers in rows, columns, and boxes
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        
        # Iterate through each cell in the board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                    
                # Calculate box index
                box_index = (i // 3) * 3 + j // 3
                
                # Check if number exists in current row, column, or box
                if (num in rows[i] or 
                    num in cols[j] or 
                    num in boxes[box_index]):
                    return False
                    
                # Add number to respective dictionaries
                rows[i][num] = True
                cols[j][num] = True
                boxes[box_index][num] = True
                
        return True

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Valid Sudoku
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(solution.isValidSudoku(board1))  # Expected: True
    
    # Test case 2: Invalid Sudoku (duplicate in row)
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(solution.isValidSudoku(board2))  # Expected: False 