class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1,c2 = 0,0
        for i in nums1:
            if i in (nums2): c1 += 1
        for i in nums2:
            if i in (nums1): c2 += 1
        return [c1,c2]