class Solution:
    def sortArrayByParity(self, n: List[int]) -> List[int]:
        x = [] ; y = []
        for i in n:
            if i%2==0:
                x.append(i)
            else:
                y.append(i)
        return x[:]+y[:]