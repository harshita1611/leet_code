# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def isleaf(root,arr):
            if not root : 
                return
            if not root.left and not root.right : 
                arr.append(root.val)
            if root.left :
                isleaf(root.left,arr)
            if root.right:
                isleaf(root.right,arr)       
            return arr
        
        x=[]
        isleaf(root1,x)
        print(x)
        y=[]
        isleaf(root2,y)
        
        return x==y
