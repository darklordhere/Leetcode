# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.fun(nums,0,len(nums))
    
    def fun(self,nums,start,end):
        if start >= end:
            return None
        else:
            return TreeNode(
            val = nums[(start+end)//2] ,
            left = self.fun(nums,start,(start+end)//2),
            right = self.fun(nums,1+((start+end)//2),end)
            )