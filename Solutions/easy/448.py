class Solution:
    
        # "for" does not support increase/reducing "i" in the loop, so I use "while"
        
        # nums: [4, 3, 2, 7, 8, 2, 3, 1]
        # after_loop_nums: [1, 2, 3, 4, 3, 2, 7, 8]
        # l: [5, 6]
        
        
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            pos = nums[i]-1      # 0 <= nums[i] - 1 = index <= n-1
            if nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i=i+1
        l = []
        for i in range(len(nums)):
            if nums[i] != i+1:      # i+1: 1 <= nums[i] <= n, 1 <= i+1 <= n 
                l.append(i+1)
        return l