class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # If needle is empty, return 0
        if not needle:
            return 0
        
        # If haystack is empty or shorter than needle, return -1
        if not haystack or len(haystack) < len(needle):
            return -1
        
        # Check each possible starting position in haystack
        for i in range(len(haystack) - len(needle) + 1):
            # If we find a match, return the index
            if haystack[i:i+len(needle)] == needle:
                return i
        
        # If no match is found, return -1
        return -1

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    haystack1 = "sadbutsad"
    needle1 = "sad"
    result1 = solution.strStr(haystack1, needle1)
    print(f"Test case 1: {result1}")  # Expected: 0
    
    # Test case 2
    haystack2 = "leetcode"
    needle2 = "leeto"
    result2 = solution.strStr(haystack2, needle2)
    print(f"Test case 2: {result2}")  # Expected: -1 