class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        x = Counter(words)
        a,b = 0,0
        for i,j in x.items():
            if i[0] == i[1]:
                a = max(a,j%2)
                b += j//2*2
            else:
                b += min(j,x[i[::-1]])
        return (a+b)*2