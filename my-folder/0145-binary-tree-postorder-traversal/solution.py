# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        def postorder(root,arr):
            if not root :
                return 
            if root :
                postorder(root.left,arr)
                postorder(root.right,arr)
                arr.append(root.val)
            return arr
        return postorder(root,arr)
