from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Find all unique combinations in candidates where the candidate numbers sum to target.
        
        Args:
            candidates: List of distinct integers
            target: Target sum to achieve
            
        Returns:
            List of all possible combinations that sum to target
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
                if candidates[i] > target:
                    # Skip candidates that would exceed target
                    continue
                    
                # Include current candidate
                current.append(candidates[i])
                # Recursive call with updated target and same start index (can reuse same number)
                backtrack(i, target - candidates[i], current)
                # Backtrack by removing the last added candidate
                current.pop()
        
        # Sort candidates for optimization
        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result 