class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c,w,a = 0,words,set(allowed)
        for i in range(len(w)):
            if not((set(w[i]))-a):
                c += 1
        return c