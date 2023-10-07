class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = nums
        ind = -1
        for i in range(len(n)-2,-1,-1):
            if n[i] < n[i+1]:
                ind = i
                break
        if ind == -1:
            n[:] = n[::-1]
        else:
            n[:] = n[:ind+1] + sorted(n[ind+1:])
            for i in range(ind+1,len(n)):
                if n[i] > n[ind]:
                    n[ind],n[i] = n[i],n[ind]
                    break
        
                