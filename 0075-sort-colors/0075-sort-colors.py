class Solution:
    def sortColors(self, l: List[int]) -> None:
        def ins(l,x):
            if len(l)==0 or l[-1]<=x: l.append(x) ; return l
            y = l[-1] ; l.pop() ; ins(l,x) ; l.append(y) ; return l
        def f1(l):
            if len(l) == 1: return l
            x = l[-1] ; l.pop() ; f1(l) ; ins(l,x) ; return l
        f1(l)