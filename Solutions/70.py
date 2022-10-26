class Solution:
    
    # Fibonacci numbers
    # n
    # n - 1
    # n - 2
    
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        f1 = 1
        f2 = 2
        for i in range(3, n+1):
            f1, f2 = f2, f1+f2
        return f2