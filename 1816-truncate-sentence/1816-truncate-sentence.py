class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        m = s.split()
        for i in m:
            m = m[:k]
        return " ".join(m)