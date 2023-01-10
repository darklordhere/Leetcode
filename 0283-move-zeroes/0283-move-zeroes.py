class Solution:
    def moveZeroes(self, n: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = n.count(0)
        while 0 in n: n.remove(0)
        else: n[:] = n+[0]*c