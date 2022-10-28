class Solution:
    
    # s="rat", t="car"
    # s="art", t="acr" = false
    
    def isAnagram(self, s: str, t: str) -> bool:
        a1 = list(s)
        a2 = list(t)
        a1.sort()
        a2.sort()
        return a1 == a2