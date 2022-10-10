class Solution:
    def breakPalindrome(self, p: str) -> str:
        if len(p) == 1: return ''
        n = len(p) ; l = list(p)
        for i in range(n // 2):
            if l[i] > 'a':
                l[i] = 'a'
                break
        else: l[-1] = 'b'
        return ''.join(l)