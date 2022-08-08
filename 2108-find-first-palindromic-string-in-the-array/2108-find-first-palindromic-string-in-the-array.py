class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        w = words
        for i in w:
            if i == i[::-1]:
                return i
        return ""