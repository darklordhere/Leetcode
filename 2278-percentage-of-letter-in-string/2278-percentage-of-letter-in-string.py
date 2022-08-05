class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        dict = Counter(s)
        return (s.count(letter) * 100) // len(s)