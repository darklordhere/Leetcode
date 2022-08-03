class Solution:
    def repeatedCharacter(self, s: str) -> str:
        x = []
        for i in s :
            if i not in x:
                x.append(i)
            else:
                return i
                
        