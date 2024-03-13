# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursion(self,root,level,result):
        if not root :
            return 
        if len(result)==level:
            result.append(root.val)
        self.recursion(root.right, level+1,result)
        self.recursion(root.left,level+1,result)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.recursion(root,0,res)
        return res
