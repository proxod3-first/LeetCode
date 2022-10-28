class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            item = d.get(target-nums[i])
            if item != None:
                return [item, i]
            d[nums[i]] = i