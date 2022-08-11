class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a, b, c = "", "", ""
        for char in firstWord:
            a += str(ord(char) - ord('a'))
        for char in secondWord:
            b += str(ord(char) - ord('a'))
        for char in targetWord:
            c += str(ord(char) - ord('a'))
        return int(a) + int(b) == int(c)