class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()
        for indx, val in enumerate(nums):
            if indx - k <= seen.get(val,-k-1): return True
            seen[val] = indx
        return False