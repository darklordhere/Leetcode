class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.max_len = 0
        def fun(s, subset):
            if s == "":
                if len(set(subset)) > self.max_len: 
                    self.max_len = len(set(subset))
                return
            for i in range(1, len(s)+1):
                subset.append(s[:i])
                fun(s[i:], subset)
                subset.remove(s[:i])
        fun(s, [])
        return self.max_len
        