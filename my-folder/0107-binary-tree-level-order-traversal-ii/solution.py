# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root is None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1
    def currLevel(self,root,level):
        if root is None :
            return []
        if level==1 :
            return [root.val]
        if level>1:
            left=self.currLevel(root.left,level-1)
            right=self.currLevel(root.right,level-1)
            return left+ right
        
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        h=self.height(root)
        for i in range(h,0,-1):
            ans.append(self.currLevel(root,i))
        return ans
