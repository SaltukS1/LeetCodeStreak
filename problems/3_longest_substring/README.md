# 3. Longest Substring Without Repeating Characters

## Problem Description

Given a string s, find the length of the longest substring without duplicate characters.

### Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

### Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

### Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring

## Constraints:
- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.

## Solution Approach

The solution uses a sliding window approach with a hash map to track character positions:

1. We maintain a sliding window using two pointers: `start` and `i`
2. As we iterate through the string, we check if the current character is already in our window
3. If it is, we move the `start` pointer to just after the previous occurrence of the character
4. We update the maximum length whenever we find a longer substring
5. We keep track of character positions in a dictionary for O(1) lookups

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(min(m, n)) where m is the size of the character set 