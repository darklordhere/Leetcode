class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x = [ nums1[i] for i in range(len(nums1)) if nums1[i] not in nums2 ]
        y = [ nums2[i] for i in range(len(nums2)) if nums2[i] not in nums1 ]
        #x , y = list(set(x)) , list(set(y))
        z =  [ list(set(x)) , list(set(y)) ]
        return z