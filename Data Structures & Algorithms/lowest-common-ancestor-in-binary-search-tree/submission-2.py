# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: 
            return None 
        if root.val < p.val: 
            if root.val < q.val: 
                root = root.right 
                return self.lowestCommonAncestor(root, p, q)
            else: 
                return root
        elif root.val == p.val:
            return root 
        else: 
            if root.val > q.val: 
                root = root.left
                return self.lowestCommonAncestor(root, p, q)
            else: 
                return root 

        