class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a,w,w2 = "",word1,word2
        for i in range(min(len(w),len(w2))):
            a += w[i]
            a += w2[i]
        if len(w) < len(w2):
            for i in range(len(w),len(w2)):
                a += w2[i]
        else:
            for i in range(len(w2),len(w)):
                a += w[i]
        return a
        