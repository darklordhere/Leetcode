class Solution:
    def findKthLargest(self, n: List[int], k: int) -> int:
        return sorted(n)[-k]