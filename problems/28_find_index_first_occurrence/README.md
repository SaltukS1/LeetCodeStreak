# 28. Find the Index of the First Occurrence in a String

## Problem Description

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.

### Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

### Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

## Constraints:
- 1 <= haystack.length, needle.length <= 10^4
- haystack and needle consist of only lowercase English characters.

## Solution Approach

The solution uses a simple sliding window approach:

1. Handle edge cases:
   - If needle is empty, return 0
   - If haystack is empty or shorter than needle, return -1

2. Check each possible starting position in haystack:
   - For each position i, check if the substring starting at i with length equal to needle matches needle
   - If a match is found, return the index i
   - If no match is found after checking all positions, return -1

Key points:
- The solution uses Python's string slicing for simplicity
- We only need to check positions where needle could fit within haystack
- The solution is straightforward but not optimized for very large strings

Time Complexity: O(m*n) where m is the length of haystack and n is the length of needle
Space Complexity: O(1) as we only use a constant amount of extra space

Note: For very large strings, more efficient algorithms like KMP (Knuth-Morris-Pratt) could be used, but this simple solution is sufficient for the given constraints. 