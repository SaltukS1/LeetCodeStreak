# 5. Longest Palindromic Substring

## Problem Description

Given a string s, return the longest palindromic substring in s.

### Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

### Example 2:
Input: s = "cbbd"
Output: "bb"

## Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.

## Solution Approach

The solution uses an expand around center approach to find the longest palindrome:

1. For each position in the string, we consider it as a potential center of a palindrome
2. We check both odd-length and even-length palindromes:
   - Odd-length: expand from a single character (e.g., "aba")
   - Even-length: expand from two characters (e.g., "abba")
3. We keep track of the longest palindrome found so far
4. We use a helper function to expand around the center and find palindrome length

Key points:
- We handle both odd and even length palindromes
- We consider each position as a potential center
- We expand around the center to find palindrome length
- We keep track of the start position and length of the longest palindrome

Time Complexity: O(n²) where n is the length of the string
Space Complexity: O(1) as we only use a constant amount of extra space 