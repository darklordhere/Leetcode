class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c = 0
        x = [ i for i in patterns if i in word]
        return len(x)