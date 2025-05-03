from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Find the smallest missing positive integer in an unsorted array.
        Must run in O(n) time and use constant extra space.
        
        Args:
            nums: List of integers (can contain negative numbers, zero, and positives)
            
        Returns:
            The smallest positive integer that is missing from the array
        """
        n = len(nums)
        
        
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                
                nums[num - 1] = -abs(nums[num - 1])
        
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        
        return n + 1 