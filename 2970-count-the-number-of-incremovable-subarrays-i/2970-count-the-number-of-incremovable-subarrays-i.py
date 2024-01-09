class Solution:
    def incremovableSubarrayCount(self, n: List[int]) -> int:
        def fn(n):
            for i in range(len(n)-1):
                if n[i] >= n[i+1]:
                    return False
            else:
                return True
            # return all(n[k]<n[k+1] for k in range(len(n)-1))
        c = 0
        for i in range(len(n)):
            for j in range(i+1,len(n)+1):
                if fn(n[:i]+n[j:]) == True:
                    c += 1
        return c