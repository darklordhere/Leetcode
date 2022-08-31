class Solution:
    def reverseWords(self, s: str) -> str:
        x,y = s.split() , []
        for i in x:
            y.append(i[::-1])
        return " ".join(y)