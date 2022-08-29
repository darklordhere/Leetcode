class Solution:
    def sortedSquares(self, n: List[int]) -> List[int]:
        x , y , l = 0 , len(n)-1 , []
        while x <= y:
            if (n[x]**2) > (n[y]**2):
                l.append(n[x]**2)
                x += 1
            else:
                l.append(n[y]**2)
                y -= 1
        return l[::-1]