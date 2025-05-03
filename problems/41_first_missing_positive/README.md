# 41. First Missing Positive

## Problem Description
Given an unsorted integer array `nums`, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

## Examples
```
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
```

```
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
```

```
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
```

## Solution Approach
The solution uses a clever approach to achieve O(n) time complexity and O(1) space:
1. First, we ignore all numbers ≤ 0 and > n (where n is array length)
2. For remaining numbers, we use the array itself as a hash table
3. Mark presence of number i by making nums[i-1] negative
4. Finally, first positive number indicates first missing positive
5. Key points:
   - Only care about numbers in range [1,n]
   - Use sign of numbers to mark presence
   - Handle duplicates carefully 