class Solution:
    def wiggleSort(self, n: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n.sort()
        
        n[::2],n[1::2] = n[:len(n[::2])][::-1],n[len(n[::2]):][::-1]