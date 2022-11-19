class Solution:
    def complexNumberMultiply(self, a1: str, b1: str) -> str:
        a,b = map(int,a1[:-1].split("+")) ; c,d = map(int,b1[:-1].split("+"))
        return str(a*c-b*d)+"+"+str(a*d+b*c)+"i"