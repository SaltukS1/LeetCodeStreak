# 29. Divide Two Integers

## Problem Description

Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing `dividend` by `divisor`.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.

### Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

### Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

## Constraints:
- -2^31 <= dividend, divisor <= 2^31 - 1
- divisor != 0

## Solution Approach

The solution uses bit manipulation and subtraction to perform division:

1. Handle edge cases:
   - If dividend is -2^31 and divisor is -1, return 2^31 - 1 (overflow case)
   - Determine the sign of the result based on the signs of dividend and divisor

2. Work with positive numbers:
   - Convert both dividend and divisor to positive numbers
   - Use bit shifting to perform efficient division

3. Main division algorithm:
   - While dividend is greater than or equal to divisor:
     - Initialize a temporary divisor and multiple
     - Double the divisor and multiple until it's too large
     - Subtract the largest multiple of divisor from dividend
     - Add the multiple to the result

4. Apply the sign to the result

Key points:
- No multiplication, division, or mod operators are used
- Bit shifting is used for efficient doubling
- Edge cases are handled properly
- The solution works within 32-bit integer constraints

Time Complexity: O(log n) where n is the absolute value of the dividend
Space Complexity: O(1) as we only use a constant amount of extra space 