class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[num] = i
        
        return []

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
    print(solution.twoSum([3, 2, 4], 6))       # Expected: [1, 2]
    print(solution.twoSum([3, 3], 6))          # Expected: [0, 1] 