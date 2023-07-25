class Solution:
    def peakIndexInMountainArray(self, ar: List[int]) -> int:
        return ar.index(max(ar))