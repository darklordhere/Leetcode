class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()
        for i in range(len(s)):
            try:
                if s[i][-1] == s[i + 1][0]: pass
                else: return False
            except:
                if s[i][-1] == s[0][0]: pass
                else: return False
        return True        