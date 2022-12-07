class Solution:
    def partitionString(self, s: str) -> int:
        x , y = set() , 1
        for i in s:
            if i in x: x.clear() ; y += 1
            x.add(i)
        return y