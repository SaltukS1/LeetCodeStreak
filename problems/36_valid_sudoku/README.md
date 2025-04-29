# 36. Valid Sudoku

## Problem Description
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

## Example
Input: board = 
```
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```
Output: true

## Solution Approach
The solution uses three sets of dictionaries to track the numbers in each row, column, and 3x3 sub-box. For each cell in the board:
1. Check if the number already exists in the current row
2. Check if the number already exists in the current column
3. Check if the number already exists in the current 3x3 sub-box

If any of these checks fail, the board is invalid. If all checks pass for all cells, the board is valid. 