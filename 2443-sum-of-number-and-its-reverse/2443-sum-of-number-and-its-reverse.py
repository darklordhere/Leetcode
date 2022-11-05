class Solution:
    def sumOfNumberAndReverse(self, n: int) -> bool:
        for i in range(n+1):
            x = i + int(str(i)[::-1])
            if x == n:
                return True
                break
        return False
            