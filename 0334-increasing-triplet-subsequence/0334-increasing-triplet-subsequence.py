class Solution:
    def increasingTriplet(self, n: List[int]) -> bool:
        n1 = n2 = inf
        for i in n:
            if i <= n1:
                n1 = i
            elif i <= n2:
                n2 = i
            else:
                return True
        return False