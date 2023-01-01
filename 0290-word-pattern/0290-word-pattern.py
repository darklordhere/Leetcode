class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        s =  s.split() ; return len(set(zip(p,s))) == len(set(p)) == len(set(s)) and len(p) == len(s)
        