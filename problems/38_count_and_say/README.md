# 38. Count and Say

## Problem Description
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

- `countAndSay(1) = "1"`
- `countAndSay(n)` is the way you would "say" the digit string from `countAndSay(n-1)`, which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character.

## Example
```
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "1211"
```

## Solution Approach
The solution uses an iterative approach:
1. Start with the base case "1" for n=1
2. For each subsequent n:
   - Count consecutive same digits in the previous result
   - Build the new string by concatenating the count and digit for each group
3. Repeat the process n-1 times
4. Key steps for each iteration:
   - Keep track of current count of consecutive digits
   - When a different digit is encountered, append the count and previous digit
   - Handle the last group separately 