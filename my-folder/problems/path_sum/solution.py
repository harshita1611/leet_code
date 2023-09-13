# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans=0
        if root is None :
            return False
        newsum=targetSum-root.val

        if newsum==0 and root.left == None and root.right==None :
            return True

        if root.left is not None :
            ans = ans or self.hasPathSum(root.left , newsum)
        if root.right is not None :
            ans = ans or self.hasPathSum(root.right , newsum)
            
        return ans