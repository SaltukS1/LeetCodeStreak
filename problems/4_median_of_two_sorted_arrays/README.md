# 4. Median of Two Sorted Arrays

## Problem Description

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

### Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

### Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5

## Solution Approach

The solution uses a binary search approach to find the median in O(log(min(m,n))) time:

1. We ensure nums1 is the shorter array to optimize the algorithm
2. We perform binary search on the shorter array
3. For each partition in nums1, we calculate the corresponding partition in nums2
4. We check if the partition is correct by comparing the boundary elements
5. If the partition is correct, we calculate the median based on whether the total length is odd or even
6. If not, we adjust the binary search range based on the comparison

Key points:
- We don't actually merge the arrays
- We use binary search to find the correct partition
- We handle both odd and even total lengths
- We use infinity values to handle edge cases

Time Complexity: O(log(min(m,n))) where m and n are the lengths of the input arrays
Space Complexity: O(1) as we only use a constant amount of extra space 