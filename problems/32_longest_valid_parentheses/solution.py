class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with -1 to handle edge cases
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        
        return max_length

# Test cases
def test_longestValidParentheses():
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.longestValidParentheses("(()") == 2
    
    # Test case 2: Nested parentheses
    assert solution.longestValidParentheses(")()())") == 4
    
    # Test case 3: Empty string
    assert solution.longestValidParentheses("") == 0
    
    # Test case 4: All valid
    assert solution.longestValidParentheses("()()()") == 6
    
    # Test case 5: Complex case
    assert solution.longestValidParentheses("()(()") == 2
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_longestValidParentheses() 