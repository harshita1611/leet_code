# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def ancestor(root,minimum,maximum):
            if not root:
                return maximum-minimum
            
            minimum=min(minimum,root.val)
            maximum=max(maximum,root.val)
            
            left_diff= ancestor(root.left,minimum,maximum)
            right_diff=ancestor(root.right,minimum,maximum)
            
            return max(left_diff,right_diff)
        
        return ancestor(root,float("inf"),float("-inf"))