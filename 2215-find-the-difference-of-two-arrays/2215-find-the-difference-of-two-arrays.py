class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x , y = [] , [] 
        y = [ nums2[i] for i in range(len(nums2)) if nums2[i] not in nums1 ]
        # for i in range(len(nums2)):
        #     if nums2[i] not in nums1:
        #         y.append(nums2[i])
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                x.append(nums1[i])
        x , y = list(set(x)) , list(set(y))
        z =  [ x , y ]
        return z