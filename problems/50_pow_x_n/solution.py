from typing import List

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle edge cases
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
            
        # Use binary exponentiation
        # If n is even: x^n = (x^2)^(n/2)
        # If n is odd: x^n = x * (x^2)^((n-1)/2)
        half = self.myPow(x * x, n // 2)
        return half * x if n % 2 else half

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.00000, 10))  # Expected: 1024.00000
    print(sol.myPow(2.10000, 3))   # Expected: 9.26100
    print(sol.myPow(2.00000, -2))  # Expected: 0.25000
    print(sol.myPow(1.00000, 2147483647))  # Expected: 1.00000
    print(sol.myPow(2.00000, -2147483648)) # Expected: 0.00000 