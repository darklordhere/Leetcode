# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s=[]
        dp=defaultdict(int)
        while root!=None or len(s):
            while root!=None:
                s.append(root)
                if dp[k-root.val]==1:
                    return True
                else:
                    dp[root.val]=1
                root=root.left
            root=s.pop()
            root=root.right