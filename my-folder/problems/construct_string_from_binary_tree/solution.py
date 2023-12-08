# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string=""
        if root==None:
            return string
        string+=str(root.val)
        # if root.left==None and root.right==None:
        #     return string
        if root.left!= None or root.right!=None :
            string+='(' + self.tree2str(root.left) + ')'
        if root.right!=None :
            string+='(' + self.tree2str(root.right) + ')'
        return string
        