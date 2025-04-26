class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
                
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # Target is in the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                # Target is in the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [4,5,6,7,0,1,2]
    target1 = 0
    print(solution.search(nums1, target1))  # Expected: 4
    
    # Test case 2
    nums2 = [4,5,6,7,0,1,2]
    target2 = 3
    print(solution.search(nums2, target2))  # Expected: -1
    
    # Test case 3
    nums3 = [1]
    target3 = 0
    print(solution.search(nums3, target3))  # Expected: -1 