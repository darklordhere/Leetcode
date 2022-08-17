class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s,sr = sentence , searchWord
        x = s.split()
        print(x)
        for i in range(0,len(x)):
            if x[i].startswith(sr):
                return x.index(x[i]) + 1
        return -1