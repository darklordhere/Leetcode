class Solution:
    def countCharacters(self, w: List[str], c: str) -> int:
        x = Counter(c) ; r = 0
        for i in w:
            if not Counter(i)-x: r += len(i)
        return r
        