class Solution:
    def makeGood(self, s: str) -> str:
        l = []
        for i in s: l.pop() if l and l[-1] == i.swapcase() else l.append(i)
        return "".join(l)