from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Find all unique combinations in candidates where the candidate numbers sum to target.
        Each number in candidates may only be used once.
        
        Args:
            candidates: List of integers (may contain duplicates)
            target: Target sum to achieve
            
        Returns:
            List of all possible unique combinations that sum to target
        """
        def backtrack(start: int, target: int, current: List[int]) -> None:
            """
            Helper function to perform backtracking.
            
            Args:
                start: Starting index in candidates to consider
                target: Remaining target sum to achieve
                current: Current combination being built
            """
            if target == 0:
                # Found a valid combination
                result.append(current[:])
                return
                
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    # Skip duplicates at same level
                    continue
                    
                if candidates[i] > target:
                    # Skip candidates that would exceed target
                    break
                    
                # Include current candidate
                current.append(candidates[i])
                # Recursive call with next index (can't reuse same number)
                backtrack(i + 1, target - candidates[i], current)
                # Backtrack by removing the last added candidate
                current.pop()
        
        # Sort candidates to handle duplicates
        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result 