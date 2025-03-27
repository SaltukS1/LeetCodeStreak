class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize variables
        result = 0
        sign = 1
        i = 0
        
        # Skip leading whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
            
        # Check sign
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = 1 if s[i] == '+' else -1
            i += 1
            
        # Read digits
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow
            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
                return 2**31 - 1 if sign == 1 else -2**31
            if result < (-2**31) // 10 or (result == (-2**31) // 10 and digit > 8):
                return -2**31
                
            result = result * 10 + digit
            i += 1
            
        return sign * result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.myAtoi("42"))  # Expected: 42
    
    # Test case 2
    print(solution.myAtoi("   -042"))  # Expected: -42
    
    # Test case 3
    print(solution.myAtoi("1337c0d3"))  # Expected: 1337
    
    # Test case 4
    print(solution.myAtoi("0-1"))  # Expected: 0
    
    # Test case 5
    print(solution.myAtoi("words and 987"))  # Expected: 0 