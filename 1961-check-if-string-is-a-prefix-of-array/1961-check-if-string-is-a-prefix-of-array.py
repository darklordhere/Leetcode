class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        c = ''
        for i in words:
            c+=i
            if (s==c):
                return True
                break
        return False