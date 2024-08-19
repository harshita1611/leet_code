# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        res=[]
        ltr=True
        q=deque([root])
        while q:
            curr_level_vals = []
            for _ in range(len(q)):
                node = q.popleft()
                curr_level_vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if not ltr:
                curr_level_vals.reverse()
            
            res.append(curr_level_vals)
            ltr = not ltr
        
        return res
