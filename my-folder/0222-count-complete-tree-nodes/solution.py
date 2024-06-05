# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        inorder=[]
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            inorder.append(root.val)
            traversal(root.right)
            return inorder
        traversal(root)
        return len(inorder)
