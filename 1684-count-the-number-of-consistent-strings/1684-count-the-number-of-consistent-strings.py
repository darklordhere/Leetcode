class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c,w,a = 0,words,set(allowed)
        for i in range(len(w)):
            s=set(w[i])
            if not (s-a):
                c += 1
        return c