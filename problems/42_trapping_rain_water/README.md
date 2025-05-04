# 42. Trapping Rain Water

## Problem Description
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Examples
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water are being trapped.
```

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Solution Approach
The solution uses a two-pointer approach to achieve O(n) time complexity and O(1) space:
1. Use two pointers (left and right) starting from both ends
2. Keep track of maximum height seen from left and right
3. For each position:
   - If left max is smaller than right max, process left side
   - Otherwise process right side
   - Add trapped water based on the difference between current height and the respective max height
4. Key points:
   - Water trapped at any point depends on minimum of max heights on both sides
   - Process the side with smaller max height first
   - No need for extra space to store left and right max arrays 