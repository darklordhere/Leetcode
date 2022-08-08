class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l,s = [] , sentences
        for i in s:
            l.append(len(i.split(' ')))
        return max(l)