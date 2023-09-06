class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        max_vowels = curr_vowels = 0
        for i, c in enumerate(s):
            if c in vowels: curr_vowels += 1
            if i >= k and s[i-k] in vowels: curr_vowels -= 1
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels
    
        # def cnt(s):
        #     x = Counter(s)
        #     r = x["a"]+x["e"]+x["i"]+x["o"]+x["u"]
        #     return r
        # i,j,m = 0,0,0
        # while j <= len(s):
        #     t = s[i:j]
        #     if len(t) == k:
        #         m = max(m,cnt(t))
        #         i += 1
        #         j += 1
        #     else:
        #         j += 1
        # return m
                
        