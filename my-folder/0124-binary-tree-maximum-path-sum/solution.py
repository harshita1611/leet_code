# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSumUtil(self,root,m):
        res=0
        if root:
            left=self.maxPathSumUtil(root.left,m)
            right=self.maxPathSumUtil(root.right,m)
            res=max(left+root.val,right+root.val,root.val)
            m[0]=max(m[0],left+right+root.val,res)
        return res

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m=[-1001]
        self.maxPathSumUtil(root,m)
        return m[0]
