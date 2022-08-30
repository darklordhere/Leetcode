class Solution:
    def rotate(self, A) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        A[:] = zip(*A[::-1])
        