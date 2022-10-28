class Solution:
    
    # Getting the previous number
    #0010=2
    #^
    #0001=1 !
    #----
    #0011=3
    #^
    #0010=2
    #----
    #0001=1 !
    
    def singleNumber(self, nums: List[int]) -> int:
        m=0
        for i in nums:
            m^=i
        return m