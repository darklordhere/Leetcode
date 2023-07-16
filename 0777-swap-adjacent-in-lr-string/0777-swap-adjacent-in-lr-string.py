class Solution:
    def canTransform(self, s: str, e: str) -> bool:
        if s.count("X") != e.count("X"):
            return False
        i = j = 0
        n = len(s)
        while i < n and j < n:
            if s[i] == "X":
                i += 1;continue
            if e[j] == "X":
                j += 1
                continue
            if s[i] != e[j] : return False
            if s[i] == "L" and i < j:
                return False
            if e[j] == "R" and i > j: return False
            i+=1 ; j+=1
        return True