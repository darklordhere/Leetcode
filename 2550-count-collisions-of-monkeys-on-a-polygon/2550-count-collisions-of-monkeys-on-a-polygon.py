class Solution:
    def monkeyMove(self, n: int) -> int:
        x = 10**9+7
        return(pow(2,n,(x))-2)%(x)