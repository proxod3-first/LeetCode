class Solution:
    
    # n = 5
    # arr = [0,0,0,0,0,0]

    # (num >> n - num decreasing number in "2^n" times; +i%2 for the first "1")
    # arr[0] = 0
    # arr[1] = arr[0] + 1%2 = 1
    # arr[2] = arr[1] + 2%2 = 1
    # arr[3] = arr[1] + 3%2 = 2
    # arr[4] = arr[2] + 4%2 = 1 (arr[4>>2=2]: 100(2)->1(2)->1(10) + 4%2 = 1(10)
    # arr[5] = arr[2] + 5%2 = 2
    
    
    def countBits(self, n: int) -> List[int]:
        arr=[0]*(n+1)
        for i in range(1, n+1):
            arr[i] = arr[i>>1] + i%2
        return arr[:n+1]
    
    
    # def countBits(self, n: int) -> List[int]:
        # return [str(bin(i)).count('1') for i in range(n+1)]