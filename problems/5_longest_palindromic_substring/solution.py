class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        start = 0
        max_length = 1
        
        # Helper function to expand around center
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
      
        for i in range(len(s)):
        
            len1 = expand_around_center(i, i)
            
            len2 = expand_around_center(i, i + 1)
            
            #
            curr_len = max(len1, len2)
            
           
            if curr_len > max_length:
                max_length = curr_len
                start = i - (curr_len - 1) // 2
        
        return s[start:start + max_length]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.longestPalindrome("babad"))  # Expected: "bab" or "aba"
    
    # Test case 2
    print(solution.longestPalindrome("cbbd"))  # Expected: "bb" 