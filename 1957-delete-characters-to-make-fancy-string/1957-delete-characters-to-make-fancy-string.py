class Solution:
    def makeFancyString(self, s: str) -> str:
        res, cnt = [s[0]], 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                res.append(s[i])
        return ''.join(res)