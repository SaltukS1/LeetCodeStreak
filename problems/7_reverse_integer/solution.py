class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Handle negative numbers
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        # Convert to string, reverse, and convert back to int
        reversed_str = str(x)[::-1]
        reversed_num = int(reversed_str) * sign
        
        # Check if the result is within 32-bit integer range
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
            
        return reversed_num

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.reverse(123))  # Expected: 321
    
    # Test case 2
    print(solution.reverse(-123))  # Expected: -321
    
    # Test case 3
    print(solution.reverse(120))  # Expected: 21 