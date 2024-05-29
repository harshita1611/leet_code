# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBSTUtil(self,node,mini,maxi):
        if node is None:
            return True
        if not(mini<node.val<maxi):
            return False
        return ((self.isBSTUtil(node.left,mini,node.val))and (self.isBSTUtil(node.right,node.val,maxi)))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mini=float('-inf')
        maxi=float('inf')
        return self.isBSTUtil(root,mini,maxi)



