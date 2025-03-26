# 7. Reverse Integer

## Problem Description

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

### Example 1:
Input: x = 123
Output: 321

### Example 2:
Input: x = -123
Output: -321

### Example 3:
Input: x = 120
Output: 21

## Constraints:
- -2^31 <= x <= 2^31 - 1

## Solution Approach

The solution uses string manipulation to reverse the digits:

1. Handle negative numbers by storing the sign and working with absolute value
2. Convert the number to string and reverse it using string slicing
3. Convert back to integer and apply the sign
4. Check if the result is within 32-bit integer range
5. Return 0 if out of range, otherwise return the reversed number

Key points:
- Handle negative numbers correctly
- Check for integer overflow
- Handle trailing zeros
- Return 0 for out-of-range results

Time Complexity: O(log|x|) where |x| is the absolute value of the input number
Space Complexity: O(log|x|) to store the string representation 