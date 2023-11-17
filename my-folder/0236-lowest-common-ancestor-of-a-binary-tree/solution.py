# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_path(curr,target,path):
            if curr is None:
                return False
            path.append(curr.val)
            if curr.val==target.val:
                return True

            left_subtree=find_path(curr.left,target,path)
            if left_subtree:
                return True
            right_subtree=find_path(curr.right,target,path)
            if right_subtree:
                return True

            path.pop()
            return False
        path_1=[]
        path_2=[]
        find_path(root,p,path_1)
        find_path(root,q,path_2)
        i=0 
        while i<len(path_1) and i<len(path_2) :
            if path_1[i]!=path_2[i]:
                break
            i+=1
        return TreeNode(path_1[i-1])
