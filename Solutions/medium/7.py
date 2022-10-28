class Solution:
    def reverse(self, x: int) -> int:
        sigh = 1;
        if x < 0:
            sigh = -1;
            x *= -1
        num = int(str(x)[::-1])
        return sigh * num if num >= pow(-2, 31) and num <= pow(2, 31) - 1 else 0