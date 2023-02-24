class Solution:
    def longestValidParentheses(self, st: str) -> int:
        s = [-1] ; m = 0
        for i,j in enumerate(st):
            if j == "(": s.append(i)
            else:
                s.pop()
                if not s: s.append(i)
                else: m = max(m,i-s[-1])
        return m