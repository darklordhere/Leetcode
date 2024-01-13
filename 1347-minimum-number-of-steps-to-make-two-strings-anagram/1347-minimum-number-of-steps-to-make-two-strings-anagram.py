class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a,b = Counter(s),Counter(t) ; c = 0
        for i in b:
            if i not in a: c += b[i]
            elif a[i]<b[i]: c += b[i]-a[i] 
        return c