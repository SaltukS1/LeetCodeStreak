class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
            
        # Create a list of strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = True
        
        # Place characters in zigzag pattern
        for char in s:
            rows[current_row] += char
            
            if going_down:
                current_row += 1
                if current_row == numRows - 1:
                    going_down = False
            else:
                current_row -= 1
                if current_row == 0:
                    going_down = True
        
        # Join all rows to get the final string
        return ''.join(rows)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.convert("PAYPALISHIRING", 3))  # Expected: "PAHNAPLSIIGYIR"
    
    # Test case 2
    print(solution.convert("PAYPALISHIRING", 4))  # Expected: "PINALSIGYAHRPI"
    
    # Test case 3
    print(solution.convert("A", 1))  # Expected: "A" 