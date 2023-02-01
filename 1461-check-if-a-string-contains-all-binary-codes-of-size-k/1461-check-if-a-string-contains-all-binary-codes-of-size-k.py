class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k: 
            return False
        x = set()
        for i in range(len(s)-k+1): 
            x.add(s[i:i+k])
        return len(x) == 2**k