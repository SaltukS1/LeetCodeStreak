class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        char_dict = {}
        max_length = 0
        start = 0
        
        for i, char in enumerate(s):
            
            if char in char_dict:
                start = max(start, char_dict[char] + 1)
            
            
            char_dict[char] = i
            
          
            max_length = max(max_length, i - start + 1)
        
        return max_length

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.lengthOfLongestSubstring("abcabcbb"))  # Expected: 3
    
    # Test case 2
    print(solution.lengthOfLongestSubstring("bbbbb"))  # Expected: 1
    
    # Test case 3
    print(solution.lengthOfLongestSubstring("pwwkew"))  