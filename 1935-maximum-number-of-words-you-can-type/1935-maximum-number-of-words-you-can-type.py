class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        t = text.split()
        l = len(t)
        b = set(brokenLetters)
        for i in t:
            for j in i:
                if j in b:
                    l -= 1
                    break
        return l