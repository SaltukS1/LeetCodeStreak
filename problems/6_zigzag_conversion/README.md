# 6. Zigzag Conversion

## Problem Description

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.

### Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

### Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
```
P     I    N
A   L S  I G
Y A   H R
P     I
```

### Example 3:
Input: s = "A", numRows = 1
Output: "A"

## Constraints:
- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'
- 1 <= numRows <= 1000

## Solution Approach

The solution uses a list of strings to simulate the zigzag pattern:

1. Create a list of empty strings for each row
2. Track the current row and direction (going down or up)
3. Place each character in the appropriate row
4. Change direction when reaching the top or bottom row
5. Finally, join all rows to get the result

Key points:
- Handle special cases (numRows = 1 or numRows >= len(s))
- Use a boolean flag to track direction
- Build the result row by row
- Join rows at the end

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) to store the characters in rows 