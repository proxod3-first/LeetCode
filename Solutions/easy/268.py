class Solution:
    
    # [3,0,1]: 2 is missing
    # sum([3,0,1,2])-sum([3,0,1])=6-4=2
    
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums)*(1+len(nums))//2 - sum(nums)