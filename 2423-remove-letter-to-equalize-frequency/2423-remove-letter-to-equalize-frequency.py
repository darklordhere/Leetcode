class Solution:
    def equalFrequency(self, word: str) -> bool:
        dct = collections.Counter(word)
        for el in word:
            dct[el]-=1
            if not dct[el]: del dct[el]
            if len(set(dct.values())) == 1: return True
            dct[el]+=1
        return False