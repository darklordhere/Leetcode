class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        c1 , c2 = '' , ''
        for i in word1:
            c1 += i
        for j in word2:
            c2 += j
        return c1 == c2