class Solution:
    def search(self, n: List[int], t: int) -> int:
        if t not in n: return -1
        else:
            x = 0
            while x != len(n):
                if n[x] == t: return x
                x+=1