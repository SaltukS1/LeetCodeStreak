class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Generate the nth term of the count-and-say sequence.
        
        Args:
            n: An integer where 1 <= n <= 30
            
        Returns:
            The nth term of the count-and-say sequence as a string
        """
        if n <= 0:
            return ""
            
        # Base case
        result = "1"
        
        # Generate sequence n-1 times
        for _ in range(n - 1):
            # Variables to build next term
            current = result[0]
            count = 1
            next_term = ""
            
            # Process current term to generate next term
            for i in range(1, len(result)):
                if result[i] == current:
                    count += 1
                else:
                    # Add count and digit to next term
                    next_term += str(count) + current
                    # Reset for next group
                    current = result[i]
                    count = 1
            
            # Handle the last group
            next_term += str(count) + current
            result = next_term
            
        return result 