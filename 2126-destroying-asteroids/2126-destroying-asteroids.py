class Solution:
    def asteroidsDestroyed(self, m: int, a: List[int]) -> bool:
        for i in sorted(a):
            if m >= i: m += i 
            else: return False
        return True
        