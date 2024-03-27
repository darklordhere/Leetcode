class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = deque(nums)
        x.rotate(k)
        nums[:] = list(x)
        