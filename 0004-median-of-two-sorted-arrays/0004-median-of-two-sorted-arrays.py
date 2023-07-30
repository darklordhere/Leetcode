class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = sorted(nums1[:] + nums2[:]) ;
        l = len(x)
        return (x[l//2]+x[(l//2)-1])/2 if l%2 == 0 else x[l//2]