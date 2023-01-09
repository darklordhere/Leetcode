class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def fun(p1,p2):
            a,b = p1 ; c,d = p2
            return ((((a-c)**2)+((b-d)**2))**0.5)
        s = set()
        s.add(fun(p1,p2));s.add(fun(p1,p3));s.add(fun(p1,p4))
        s.add(fun(p2,p3));s.add(fun(p2,p4));s.add(fun(p3,p4))
        if 0 in s: return False
        else: return len(s) == 2

        

        