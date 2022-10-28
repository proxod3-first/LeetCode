class Solution:
    
    # n = 00000000000000000000000000001011
    # count('1') = 3
    
    
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')