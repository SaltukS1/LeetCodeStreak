class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Multiply two numbers represented as strings.
        
        Args:
            num1: First number as string
            num2: Second number as string
            
        Returns:
            Product of num1 and num2 as string
        """
        if num1 == "0" or num2 == "0":
            return "0"
            
        # Initialize result array with zeros
        result = [0] * (len(num1) + len(num2))
        
        # Iterate from right to left for both numbers
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                # Convert characters to integers
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                # Calculate current position and carry position
                curr_pos = i + j + 1
                carry_pos = i + j
                
                product = digit1 * digit2 + result[curr_pos]
                
              
                result[curr_pos] = product % 10
                result[carry_pos] += product // 10
        
       
        result_str = ""
        start_idx = 0
        while start_idx < len(result) and result[start_idx] == 0:
            start_idx +=  1
            

        result_str = "".join(map(str, result[start_idx:]))
        
        return result_str if result_str else "0"

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.multiply("2", "3") == "6"
    
    # Test case 2
    assert solution.multiply("123", "456") == "56088"
    
    # Test case 3
    assert solution.multiply("0", "0") == "0"
    
    print("All test cases passed!") 