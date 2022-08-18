class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        a = dict()
        b = -1
        for i, j in enumerate(s):
            if j not in a:
                a[j] = i
            else:
                b = max(b, i - a[j] -1)
                print(b)
        return b
