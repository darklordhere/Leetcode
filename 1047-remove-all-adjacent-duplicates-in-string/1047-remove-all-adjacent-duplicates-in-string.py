class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = []
        for i in s: l.pop() if l and l[-1] == i else l.append(i)
        return "".join(l)