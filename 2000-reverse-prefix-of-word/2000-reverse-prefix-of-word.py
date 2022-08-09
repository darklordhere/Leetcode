class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        f = word.find(ch)    
        return word[:f + 1][::-1] + word[f + 1:]