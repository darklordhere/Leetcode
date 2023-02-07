class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [ x for pair in zip(nums[:len(nums)//2],nums[len(nums)//2:]) for x in pair]