class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # maxSum = currentSum = nums[0]  
        # for i in range(1, len(nums)):
        #     currentSum = max(nums[i] + currentSum, nums[i]) # has it been worse or not?
        #     maxSum = max(currentSum, maxSum) 
        # return maxSum
        
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)