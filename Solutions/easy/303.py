class NumArray:

    # nums: [-2, 0, 3, -5, 2, -1]
    # prefSum: [-2, -2, 1, -4, -2, -3]
    
    
    def __init__(self, nums: List[int]):
        prefSum = []
        currentSum = 0
        for i in nums:
            currentSum += i
            prefSum.append(currentSum)
        self.prefSum = prefSum

    def sumRange(self, left: int, right: int) -> int:
        if left == 0: 
            return self.prefSum[right]
        return self.prefSum[right] - self.prefSum[left-1]    # (r)-(l-1)=r+1-l
                                                             # (r+1)-(l)=r+1-l
    
    
    
    # def __init__(self, nums: List[int]):
    #     self.nums = nums
    
    # def sumRange(self, left: int, right: int) -> int:
    #     return sum(self.nums[left:right+1])
    
    
    