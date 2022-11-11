class Solution:
    def removeDuplicates(self, n: List[int]) -> int:
        n[:] = sorted(list(set(n)))
        return len(n)