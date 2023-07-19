class Solution:
    def searchRange(self, n: List[int], t: int) -> List[int]:
        if t not in n:
            return [-1,-1]
        else:
            a,b = 0,0
            for i in range(len(n)):
                if n[i] == t:
                    a = i
                    break
            n = n[::-1]
            for i in range(len(n)):
                if n[i] == t:
                    b = len(n)-i-1
                    break
            return [a,b]