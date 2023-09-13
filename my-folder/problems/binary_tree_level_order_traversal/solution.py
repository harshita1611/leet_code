# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def height(root):
            if root is None :
                return 0
            left_height= height(root.left)
            right_height=height(root.right)

            if left_height > right_height :
                return left_height + 1
            else :
                return right_height +1 

        def currentlevel(root,level) :
            if root is None :
                return [] 
            if level==1 :
                return [root.val]
            elif level > 1 :
                left_values=currentlevel(root.left , level-1)
                right_values=currentlevel(root.right , level-1)
                return left_values + right_values
        
        arr = []
        h = height(root)
        for i in range(1, h + 1):
            level_values = currentlevel(root, i)
            if level_values:
                arr.append(level_values)
        return arr