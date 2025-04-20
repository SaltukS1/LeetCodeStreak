class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Initialize a pointer for the position to place non-val elements
        k = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is not equal to val
            if nums[i] != val:
                # Place it at position k
                nums[k] = nums[i]
                # Increment k
                k += 1
        
        # Return the number of elements not equal to val
        return k

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    print(f"Test case 1: k = {k1}, nums = {nums1[:k1]}")  # Expected: k = 2, nums = [2, 2]
    
    # Test case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print(f"Test case 2: k = {k2}, nums = {nums2[:k2]}")  # Expected: k = 5, nums = [0, 1, 4, 0, 3] 