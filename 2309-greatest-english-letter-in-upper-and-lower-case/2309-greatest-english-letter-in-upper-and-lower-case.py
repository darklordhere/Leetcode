class Solution:
    def greatestLetter(self, s: str) -> str:
        c = ''
        for i in s:
            if i.isupper() and i.lower() in s:
                if i > c :
                    c = i.upper()
        return c