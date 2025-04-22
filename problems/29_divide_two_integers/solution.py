class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        while dividend >= divisor:
            # Initialize the temp divisor and multiple
            temp_divisor = divisor
            multiple = 1
            
            # Double the divisor and multiple until it's too large
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # Subtract the largest multiple of divisor from dividend
            dividend -= temp_divisor
            result += multiple
        
        # Apply the sign
        if negative:
            result = -result
        
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    dividend1 = 10
    divisor1 = 3
    result1 = solution.divide(dividend1, divisor1)
    print(f"Test case 1: {result1}")  # Expected: 3
    
    # Test case 2
    dividend2 = 7
    divisor2 = -3
    result2 = solution.divide(dividend2, divisor2)
    print(f"Test case 2: {result2}")  # Expected: -2
    
    # Test case 3 (edge case)
    dividend3 = -2**31
    divisor3 = -1
    result3 = solution.divide(dividend3, divisor3)
    print(f"Test case 3: {result3}")  # Expected: 2**31 - 1 