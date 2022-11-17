class Solution:
    def numOfPairs(self, n: List[str], t: str) -> int:
        c = 0
        for i in range(len(n)-1):
            for j in range(i+1,len(n)):
                if n[i]+n[j] == t: c += 1
                if n[j]+n[i] == t: c += 1
        return c