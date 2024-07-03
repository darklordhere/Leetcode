class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # l = []
        # for i in nums1:
        #     if i in nums2:
        #         l.append(i)
        #         nums2.remove(i)
        # return l
        
        return (Counter(nums1)&Counter(nums2)).elements()