from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(perm, used, res, nums):
            if (len(perm) == len(nums)):
                res.append(perm[:])
                return
            for i, num in enumerate(nums):
                if (used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1])):
                    continue
                perm.append(num)
                used[i] = True
                backtrack(perm, used, res, nums)
                perm.pop()
                used[i] = False

        nums.sort()
        res = []
        backtrack([], [False] * (len(nums)), res, nums)
        return res

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.permuteUnique([1, 1, 2]))  # Expected: [[1,1,2], [1,2,1], [2,1,1]]
    print(sol.permuteUnique([1, 2, 3]))  # Expected: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]] 