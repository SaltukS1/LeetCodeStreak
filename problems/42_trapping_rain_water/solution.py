from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculate how much water can be trapped after raining.
        
        Args:
            height: List of non-negative integers representing elevation map
            
        Returns:
            Total units of water that can be trapped
        """
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        total_water = 0
        
        while left < right:
            # Process the side with smaller max height
            if left_max <= right_max:
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
                right -= 1
        
        return total_water 