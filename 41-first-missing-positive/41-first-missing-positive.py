class Solution:
    def firstMissingPositive(self, n):
        m = 1
        for i in sorted(n):
            if i == m:
                m+=1
        return m