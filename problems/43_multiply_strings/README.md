# 43. Multiply Strings

## Problem Description
Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.


## Examples
```
Input: num1 = "2", num2 = "3"
Output: "6"
```

```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

## Constraints
- 1 <= num1.length, num2.length <= 200
- num1 and num2 consist of digits only
- Both num1 and num2 do not contain any leading zero, except the number 0 itself

## Solution Approach
1. Initialize a result array of size `len(num1) + len(num2)` with zeros (maximum possible length of product)
2. Iterate through each digit of both numbers from right to left:
   - For each pair of digits, multiply them and add to the corresponding position in result
   - Handle carry-overs appropriately
3. Convert the result array to string, removing leading zeros if any
4. Key points:
   - Process digits one by one like manual multiplication
   - Handle carry-overs carefully
   - Consider edge cases (zeros, single digits)
   - Time complexity: O(n*m) where n and m are lengths of input strings
   - Space complexity: O(n+m) for the result array.