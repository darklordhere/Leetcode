class Solution:
    def search(self, n: List[int], t: int) -> bool:
        # if target not in nums:
        #     return False
        # else:
        #     return True
        if len(n) < 2:
            return n[0] == t
        else:
            n.sort()
            x,y = 0 , len(n)-1
            while x <= y:
                m = x+(y-x)//2
                if n[m] == t:
                    return True
                elif n[m] > t:
                    y = m - 1
                else:
                    x = m + 1
            return 0