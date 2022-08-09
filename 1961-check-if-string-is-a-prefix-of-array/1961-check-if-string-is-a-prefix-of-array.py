class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        c = ''
        for i in words:
            c+=i
            if (s==c) :
                return True
            if (len(s) == len(words[0])) and (words[0] in s):
                return True
        return False