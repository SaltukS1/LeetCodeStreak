class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

# Test cases
def test_searchInsert():
    solution = Solution()
    
    # Test case 1: Target exists in the array
    assert solution.searchInsert([1,3,5,6], 5) == 2
    
    # Test case 2: Target should be inserted at the end
    assert solution.searchInsert([1,3,5,6], 7) == 4
    
    # Test case 3: Target should be inserted at the beginning
    assert solution.searchInsert([1,3,5,6], 0) == 0
    
    # Test case 4: Target should be inserted in the middle
    assert solution.searchInsert([1,3,5,6], 2) == 1
    
    # Test case 5: Empty array
    assert solution.searchInsert([], 5) == 0
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_searchInsert() 