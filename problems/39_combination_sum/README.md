# 39. Combination Sum

## Problem Description
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

## Example
```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 + 2 + 3 = 7
7 = 7
```

```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

## Solution Approach
The solution uses a backtracking approach:
1. Sort the candidates array to handle duplicates and optimize
2. Use recursive backtracking to:
   - Keep track of current sum and combination
   - For each candidate, try adding it to current combination
   - If sum equals target, add combination to result
   - If sum exceeds target, backtrack
3. Key optimizations:
   - Sort candidates to avoid duplicate combinations
   - Skip candidates that would exceed target
   - Allow reuse of same number by keeping same index 