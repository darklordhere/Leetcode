class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        l, r = 0, len(n)-1
        while l < r:
            s = n[l] + n[r]
            if s == t:
                return [l+1, r+1]
            elif s < t:
                l += 1
            else:
                r -= 1