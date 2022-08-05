class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c1,c2 = Counter(s),Counter(target)
        return min(c1[x]//c2[x] for x in target)