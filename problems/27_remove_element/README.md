# 27. Remove Element

## Problem Description

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

1. Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
2. Return `k`.

### Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

### Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

## Constraints:
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

## Solution Approach

The solution uses a two-pointer technique:

1. Initialize a pointer `k` to keep track of the position where the next non-val element should be placed.
2. Iterate through the array with another pointer `i`.
3. If the current element is not equal to `val`, place it at position `k` and increment `k`.
4. After the iteration, `k` will represent the number of elements not equal to `val`.

Key points:
- The solution modifies the array in-place.
- The order of elements may be changed.
- We only care about the first `k` elements after the operation.

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) as we modify the array in-place 