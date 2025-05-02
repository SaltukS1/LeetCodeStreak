# 40. Combination Sum II

## Problem Description
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note**: The solution set must not contain duplicate combinations.

## Example
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

```
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
```

## Solution Approach
The solution uses a backtracking approach similar to Combination Sum I, but with key differences:
1. Sort the candidates array to handle duplicates efficiently
2. Use recursive backtracking to:
   - Keep track of current sum and combination
   - For each candidate, try adding it to current combination
   - If sum equals target, add combination to result
   - If sum exceeds target, backtrack
3. Key differences from Combination Sum I:
   - Each number can only be used once (increment index in recursive call)
   - Skip duplicate combinations by skipping same value at same level
   - Check for duplicates when adding to result 