class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x,y = '',[]
        for i in digits:
            x += str(i)
        m = str(int(x) + 1)
        for i in m:
            y.append(int(i))
        return y
            
        