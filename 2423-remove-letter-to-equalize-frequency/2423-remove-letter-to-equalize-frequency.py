class Solution:
    def equalFrequency(self, w: str) -> bool:
        for i in range(len(w)):
            if len(set(Counter(w[:i]+w[i+1:]).values())) == 1:
                return True
        return False