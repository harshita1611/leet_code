# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nums=[]
        def inorder(root):
            if root :
                inorder(root.left)
                nums.append(root.val)
                inorder(root.right)
        
        inorder(root)
        diff = nums[1]-nums[0]
        for i in range(2,len(nums)):
            diff = min(diff , nums[i]-nums[i-1])
        return diff